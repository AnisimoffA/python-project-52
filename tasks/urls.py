from tasks.views import TaskList, TaskPage, TaskCreate, TaskUpdate, TaskDelete # NOQA E501
from django.urls import path

urlpatterns = [
    path('', TaskList.as_view(), name="task_list"),
    path('<int:pk>/', TaskPage.as_view(), name="task_page"),
    path('create/', TaskCreate.as_view(), name="task_create"),
    path('<int:pk>/update/', TaskUpdate.as_view(), name="task_update"),
    path('<int:pk>/delete/', TaskDelete.as_view(), name="task_delete"),
]
