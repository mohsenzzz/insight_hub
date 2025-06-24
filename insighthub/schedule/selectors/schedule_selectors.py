from rest_framework.exceptions import ValidationError

from insighthub.schedule.models import Schedule


def get_User_schedules(user_id:int):

    try:
        schedules = Schedule.objects.filter(user__id=user_id)
        return schedules
    except Exception as e:
        raise ValidationError(f"can not get schedulers: {e}")


def get_schedule_by_id(schedule_id:int):
    """
    get user schedule by id
    :param
        schedule_id: schedule id for get it from database
    :return:
       return schedule instance
    """
    try:
        return Schedule.objects.get(id=schedule_id)
    except Exception as e:
        raise ValidationError(f"schedule by id {schedule_id} not found.")