from django.contrib import admin
from django.urls import path
from tasks.views import *
from django.urls import path, include

urlpatterns = [
    path('', TaskList.as_view(), name="task_list"),
    path('<int:pk>/', TaskPage.as_view(), name="task_page"),
    path('create/', TaskCreate.as_view(), name="task_create"),
    path('<int:pk>/update/', TaskUpdate.as_view(), name="task_update"),
    path('<int:pk>/delete/', TaskDelete.as_view(), name="task_delete"),
]