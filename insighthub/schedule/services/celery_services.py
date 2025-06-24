import json
import uuid
from django.db import transaction
from rest_framework.exceptions import ValidationError
from django_celery_beat.models import PeriodicTask,CrontabSchedule

from insighthub.schedule.models import Schedule
from insighthub.tasks.models import TaskInput


def create_celery_task_schedule( cron_expression:str)->CrontabSchedule:

    minute,hour, day_of_month,month_of_year, day_of_week = cron_expression.split()
    schedule,_= CrontabSchedule.objects.get_or_create(
        minute=minute,
        hour=hour,
        day_of_month=day_of_month,
        month_of_year=month_of_year,
        day_of_week=day_of_week,
        timezone='Asia/Tehran',
    )
    return schedule



def create_periodic_task(schedule:Schedule):
    crontab_schedule= create_celery_task_schedule(schedule.cron_expression)
    try:
        with transaction.atomic():
            periodic_task = PeriodicTask.objects.create(
                crontab=crontab_schedule,
                name=schedule.task.name+"_"+str(uuid.uuid4()),
                task=f'insighthub.tasks.tasks.{schedule.task.name}',
                args=json.dumps(list(schedule.arguments.values())),
                one_off=False,
                enabled=schedule.enabled,
            )
            schedule.periodic_task = periodic_task
            schedule.save()

    except Exception as e:
        raise ValidationError(f"can not create periodic task")