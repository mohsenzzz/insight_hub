
from django.db import models
from insighthub.common.models import BaseModel
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(BaseModel, AbstractUser):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)


    USERNAME_FIELD= 'username'

    def __str__(self):
        return self.username


