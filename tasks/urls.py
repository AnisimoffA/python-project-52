from django.contrib import admin
from django.urls import path
from tasks.views import *
from django.urls import path, include

urlpatterns = [
    path('', TasksList.as_view(), name="tasks_list"),
]