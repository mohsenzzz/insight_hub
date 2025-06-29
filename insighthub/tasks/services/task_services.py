from rest_framework.exceptions import ValidationError
from django.db import transaction

from insighthub.tasks.interfaces.task_interface import TaskCreatePutInterface
from insighthub.tasks.models import Task, TaskInput
from insighthub.utils.convert_value_type import convert_value_type


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

def get_inputs(task:Task, user_inputs:dict):
    final_args = []
    for task_input in task.task_inputs.all():
        if user_inputs.get(task_input.name):
            value = user_inputs.get(task_input.name)
            final_args.append(convert_value_type(value, task_input.type))
        else:
            raise ValidationError(f"there is not agrgument {task_input.name}")
    return final_args