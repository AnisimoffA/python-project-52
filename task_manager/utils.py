from django.db.models import Count
from django.shortcuts import redirect
from django.http import Http404
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from .models import *
from tasks.models import *

menu = [{'title': "Пользователи", 'url_name': 'users_list'},
        {'title': "Статусы", 'url_name': 'statuses_list'},
        {'title': "Метки", 'url_name': 'labels_list'},
        {'title': "Задачи", 'url_name': 'task_list'},
        {'title': "Вход", 'url_name': 'login'},
        {'title': "Регистрация", 'url_name': 'users_register'},
        {'title': "Выход", 'url_name': 'logout'},
]

class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if self.request.user.is_authenticated:
            user_menu.pop(4)
            user_menu.pop(4)

        if not self.request.user.is_authenticated:
            user_menu.pop(1)
            user_menu.pop(1)
            user_menu.pop(1)
            user_menu.pop(3)

        context['menu'] = user_menu
        return context


class CustomUserPermisionsMixin:

    def has_permissions(self):
        print(self.get_object().username)
        return self.get_object().username == self.request.user.username
    
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            messages.warning(request, "У вас нет прав для изменения другого пользователя.")
            return redirect('users_list')
        return super().dispatch(request, *args, **kwargs)
    

class CustomTaskPermisionsMixin:

    def has_permissions(self):
        return self.get_object().creator.first_name == self.request.user.first_name
    
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            messages.warning(request, "Задачу может удалить только ее автор")
            return redirect('task_list')
        return super().dispatch(request, *args, **kwargs)
    

class CheckUsersTasksMixin:
    
    def has_permissions(self):
        user_id = self.request.user.id
        if Task.objects.filter(creator__id=user_id).exists():
            return False
        return True
    
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            messages.warning(request, "Пользователь используется")
            return redirect('task_list')
        return super().dispatch(request, *args, **kwargs)