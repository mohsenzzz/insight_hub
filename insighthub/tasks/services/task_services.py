from rest_framework.exceptions import ValidationError
from django.db import transaction

from insighthub.tasks.interfaces.task_interface import TaskCreatePutInterface
from insighthub.tasks.models import Task, TaskInput


def create_task(task_interfaces: TaskCreatePutInterface)->Task:
    """
    create new task
    :param
        task_interfaces: task interface that contains new data
    :return:
        return created new task
    """

    try:
        with transaction.atomic():
            task =Task.objects.create(name=task_interfaces.name,
                                description=task_interfaces.description,
                                )
            for task_input in task_interfaces.taskInput:
                TaskInput.objects.create(task=task, name=task_input.name, type=task_input.type)

        return task
    except Exception as e:
        raise ValidationError(f"can not create task {task_interfaces.name}: {e}")