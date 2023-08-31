from django.contrib import admin
from django.urls import path
from users.views import *
from django.urls import path, include

urlpatterns = [
    path('', UserList.as_view(), name="users_list"),
    path('register/', UserRegister.as_view(), name="users_register"),
    path('<int:pk>/update/', UserUpdate.as_view(), name="users_update"),
    path('<int:pk>/delete/', UserDelete.as_view(), name="users_delete"),
]