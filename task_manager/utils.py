from django.db.models import Count
from django.shortcuts import redirect
from django.http import Http404
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from .models import *

menu = [{'title': "Пользователи", 'url_name': 'users_list'},
        {'title': "Статусы", 'url_name': 'statuses_list'},
        {'title': "Метки", 'url_name': 'labels_list'},
        {'title': "Задачи", 'url_name': 'tasks_list'},
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
        return self.get_object().username == self.request.user.username
    
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            messages.error(request, "У вас нет прав для изменения другого пользователя.")
            return redirect('users_list')
        return super().dispatch(request, *args, **kwargs)