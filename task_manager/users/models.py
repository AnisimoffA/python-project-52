from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUsers(AbstractUser):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
