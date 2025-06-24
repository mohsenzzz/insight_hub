import json


from django.db import transaction
from rest_framework.exceptions import ValidationError

from insighthub.schedule.interfaces.schedule_interface import ScheduleInterface, SchedulePatchInterface
from insighthub.schedule.models import Schedule

from insighthub.tasks.selectors.task_selectors import get_task_by_id
from insighthub.users.models import User


def create_schedule(schedule_interface:ScheduleInterface, user:User, task_id:int):
    if schedule_interface.enabled and user.schedules.filter(enabled =True).count() == 5:
        raise ValidationError(f"you have 5 active schedules.")
    try:
        task = get_task_by_id(task_id)

        schedule=Schedule.objects.create(task=task,
                                         user=user,
                                         cron_expression= schedule_interface.cron_expression,
                                         enabled= schedule_interface.enabled,
                                         arguments=schedule_interface.arguments)
        return schedule
    except Exception as e:
        raise ValidationError(f"can not create schedule {schedule_interface.cron_expression}: {e}")

def partial_update_schedule(schedule_interface:SchedulePatchInterface, schedule:Schedule, user:User)->Schedule:
    """
    update schedule in database and celery
    :param schedule_interface: interface data for update
    :param schedule: schedule instance that will update
    :param user: user that request for update
    :return:
        return schedule updated
    """
    if schedule_interface.enabled and user.schedules.filter(enabled=True).count() == 5:
        raise ValidationError(f"you have 5 active schedules.")
    try:
        with transaction.atomic():
            if schedule_interface.enabled is not None:
                schedule.enabled = schedule_interface.enabled
                schedule.periodic_task.enabled = schedule_interface.enabled

            if schedule_interface.arguments is not None:
                schedule.arguments = schedule_interface.arguments
                schedule.periodic_task.args = json.dumps(list(schedule_interface.arguments.values()))




            schedule.save()
            schedule.periodic_task.save()
        return schedule
    except Exception as e:
        raise ValidationError(f"can not update schedule :{e}.")

def delete_schedule(schedule:Schedule):

    try:
        schedule.delete()
    except Exception as e:
        raise ValidationError(f"can not delete schedule: {e}")