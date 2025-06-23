from django.db import models

from insighthub.common.models import BaseModel
from insighthub.tasks.models import Task
from insighthub.users.models import User


# Create your models here.


class Schedule(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="schedules")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schedules")
    cron_expression = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)
    arguments= models.JSONField(null=True, blank=True)


