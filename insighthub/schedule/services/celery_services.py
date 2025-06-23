import json
import uuid

from django_celery_beat.models import PeriodicTask,CrontabSchedule

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



def create_periodic_task(cron_expression:str, task_name:str,enable:bool, args:dict):
    schedule= create_celery_task_schedule(cron_expression)

    PeriodicTask.objects.create(
        crontab=schedule,
        name=task_name+"_"+str(uuid.uuid4()),
        task=f'tasks.tasks.{task_name}',
        args=args,
        one_off=False,
        enabled=enable,
    )