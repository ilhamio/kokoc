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


@app.task
def recalculate():
    today = date.today()
    cursor = connection.cursor()

    # return step_count, distance, time, kcal, user_id
    cursor.execute(
        f"SELECT sum(step_count), sum(distance), sum(time), sum(kcal), user_id FROM activity_activitysnapshot WHERE date_part('day', created_at) =1 and date_part('month', created_at) = {today.month} and date_part('year',created_at) = {today.year} GROUP BY user_id")
    from activity.models import ActivityConverter
    from charity.models import Wallet

    config = ActivityConverter.objects.filter(is_active=True)
    if not len(config):
        return
    config = config[0]
    for i in cursor.fetchall():
        wallet = Wallet.objects.get(user_id=i[-1])
        summa = config.step_count * i[0] + config.distance * i[1] + config.time * i[2] + config.kcal * i[3]
        wallet.balance += summa
        wallet.save()

@app.task
def subs():
    from charity.models import CharitySubscription
    subs = CharitySubscription.objects.all()

    # if not len(config):
    #     return
    # config = config[0]
    # for i in cursor.fetchall():
    #     wallet = Wallet.objects.get(user_id=i[-1])
    #     summa = config.step_count * i[0] + config.distance * i[1] + config.time * i[2] + config.kcal * i[3]
    #     wallet.balance += summa
    #     wallet.save()