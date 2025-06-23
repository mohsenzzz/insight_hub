from rest_framework.exceptions import ValidationError

from insighthub.tasks.models import Task


def get_unschedule_tasks()->list[Task]:
    """
    get all tasks that don't have schedule
    :return:
        return list of tasks
    """
    try:
        tasks =Task.objects.all()
        return tasks
    except Exception as e:
        raise ValidationError(f"can not fetch tasks: {e}")