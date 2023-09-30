import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dobriki.settings")

app = Celery("dobriki")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()