from django.contrib import admin
from django.urls import path
from labels.views import *
from django.urls import path, include

urlpatterns = [
    path('', LabelsList.as_view(), name="labels_list"),
]