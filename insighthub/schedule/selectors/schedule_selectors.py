from rest_framework.exceptions import ValidationError

from insighthub.schedule.models import Schedule


def get_User_schedules(user_id:int):

    try:
        schedules = Schedule.objects.filter(user__id=user_id)
        return schedules
    except Exception as e:
        raise ValidationError(f"can not get schedulers: {e}")