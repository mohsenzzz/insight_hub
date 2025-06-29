from django.db import models

from insighthub.common.models import BaseModel
from insighthub.tasks.models import Task
from insighthub.users.models import User
from django_celery_beat.models import PeriodicTask


# Create your models here.


class Schedule(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="schedules")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schedules")
    periodic_task = models.ForeignKey(PeriodicTask, on_delete=models.CASCADE, null=True, blank=True)
    cron_expression = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)
    arguments= models.JSONField(null=True, blank=True)


    # def delete(self,*args, **kwargs):
    #     if self.periodic_task:
    #         self.periodic_task.delete()
    #     super().delete(*args, **kwargs)