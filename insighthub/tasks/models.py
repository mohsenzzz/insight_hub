from django.db import models

from insighthub.common.models import BaseModel
from insighthub.users.models import User


# class Schedule(BaseModel):
#     cron_expression = models.CharField(max_length=100)
#     user= models.ForeignKey(User,on_delete=models.CASCADE, related_name='schedules')

# Create your models here.
class Task(BaseModel):
    name= models.CharField(max_length=255)
    description= models.TextField(null=True,blank=True)

    # schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, related_name='tasks',null=True,blank=True)


class TaskInput(models.Model):
    TYPE_CHOICE= (
    ('string', 'String'),
    ('integer', 'Integer'),
    ('float', 'Float'),
    ('boolean', 'Boolean'),
    )

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="task_inputs")
    name=models.CharField(max_length=255)
    type = models.CharField(max_length=100, choices=TYPE_CHOICE)



    def __str__(self):
        return f"{self.name} : {self.type}"