from django.contrib import admin
from django.urls import path
from labels.views import *
from django.urls import path, include

urlpatterns = [
    path('', LabelsList.as_view(), name="labels_list"),
    path('create/', LabelCreate.as_view(), name="label_create"),
    path('<int:pk>/update/', LabelUpdate.as_view(), name="label_update"),
    path('<int:pk>/delete/', LabelDelete.as_view(), name="label_delete"),
]