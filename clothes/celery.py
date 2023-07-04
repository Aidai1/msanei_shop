# django_celery/celery.py

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clothes.settings")
app = Celery("clothes")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "send_message_to_user_tg_task-every-10-seconds": {
        'task': 'main.tasks.send_message_to_user_tg_task',
        # отправлять сообщение каждый четверг в 15:00
        'schedule': crontab(day_of_week=3, hour=7, minute=18),
    }
}