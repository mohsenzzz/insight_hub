from rest_framework.exceptions import ValidationError

from insighthub.schedule.interfaces.schedule_interface import ScheduleInterface
from insighthub.schedule.models import Schedule

from insighthub.tasks.selectors.task_selectors import get_task_by_id
from insighthub.users.models import User


def create_schedule(schedule_interface:ScheduleInterface, user:User, task_id:int):


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