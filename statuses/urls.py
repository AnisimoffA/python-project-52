from django.contrib import admin
from django.urls import path
from statuses.views import *
from django.urls import path, include

urlpatterns = [
    path('', StatusesList.as_view(), name="statuses_list"),
]