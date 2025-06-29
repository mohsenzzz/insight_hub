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

def get_task_by_id(task_id:int)->Task:

    try:
        return Task.objects.get(id=task_id)
    except Exception as e:
        raise ValidationError(f"task by id {task_id} not found.")

def get_task_by_name(task_name:str)->Task:
    try:
        return Task.objects.get(name=task_name)
    except Exception as e:
        raise ValidationError(f"task by id {task_name} not found.")