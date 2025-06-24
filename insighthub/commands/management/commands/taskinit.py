import json
import os

from django.core.management.base import BaseCommand

from config.env import BASE_DIR
from insighthub.tasks.models import Task, TaskInput


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = os.path.join(BASE_DIR, "data", "tasks.json")
        with open(file_path) as f:
            tasks = json.load(f)
            for key,value in tasks.items():
                task_params = value
                task =Task.objects.create(name=task_params['name'],description=task_params["description"] )
                if task_params.get("task_input"):
                    TaskInput.objects.create(task=task, name= task_params["task_input"]["name"], type=task_params["task_input"]["type"])

        print("tasks created successfully.")