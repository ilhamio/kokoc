import os
from datetime import date

from celery import Celery
from celery.schedules import crontab
from django.db import connection


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dobriki.settings")

app = Celery("dobriki")
app.config_from_object("django.conf:settings", namespace="CELERY")


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=5, minute=30),
        recalculate.s(),
    )
    sender.add_periodic_task(
        crontab(hour=7, minute=30),
        subs.s(),
    )


@app.task
def recalculate():
    today = date.today()
    cursor = connection.cursor()

    # return step_count, distance, time, kcal, user_id
    cursor.execute(
        f"SELECT sum(step_count), sum(distance), sum(time), sum(kcal), sum(found), activity_type, user_id FROM activity_activitysnapshot WHERE date_part('day', created_at) =1 and date_part('month', created_at) = {today.month} and date_part('year',created_at) = {today.year} GROUP BY user_id, activity_type")
    from activity.models import ActivityConverter
    from charity.models import Wallet

    config = ActivityConverter.objects.filter(is_active=True)
    config_map = dict()
    for i in config:
        config_map[i.pk] = i

    for i in cursor.fetchall():
        wallet = Wallet.objects.get(user_id=i[-1])
        act = config_map.get(i[-2])
        if act:
            summa = int(config.step_count * i[0] + config.distance * i[1] + config.time * i[2] + config.kcal * i[3] + 2 * i[4])
        else:
            summa = int(0.01 * i[0] + 0.01 * i[1] + 0.001 * i[2] + 0.012 * i[3] + 2 * i[4])
        wallet.balance += summa
        wallet.save()


@app.task
def subs():
    from charity.models import Transaction
    from charity.models import CharitySubscription
    subsc = CharitySubscription.objects.all()

    if not len(subsc):
        return

    for i in subsc:
        user = i.user
        wallet = user.wallet
        fund = i.charity

        summa = wallet.balance
        fund.sum += summa
        fund.save()
        wallet.balance = 0
        wallet.save()

        Transaction.objects.create(user_id=user.id, sum=summa, fund_id=fund.id)
