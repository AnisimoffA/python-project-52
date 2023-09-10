from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy


# Create your models here.
class CustomUsers(AbstractUser):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.first_name
