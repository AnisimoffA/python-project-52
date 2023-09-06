from django.contrib import admin
from django.urls import path
from statuses.views import *
from django.urls import path, include

urlpatterns = [
    path('', StatusesList.as_view(), name="statuses_list"),
    path('create/', StatusesCreate.as_view(), name="statuses_create"),
    path('<int:pk>/update/', StatusesUpdate.as_view(), name="statuses_update"),
    path('<int:pk>/delete/', StatusesDelete.as_view(), name="statuses_delete"),
]