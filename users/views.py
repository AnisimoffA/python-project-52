from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django import forms
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from task_manager.utils import *
from users.forms import *
from users.models import *
# Create your views here.


class UserList(DataMixin, ListView):
    model = CustomUsers
    template_name = "users/users_list.html"
    context_object_name = "users"
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Пользователи")
        return context | c_def

    def get_queryset(self):
        return CustomUsers.objects.all()


class UserRegister(DataMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = "register_form.html"
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Регистрация")
        return context | c_def
    
    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно зарегистрирован")
        form.save()
        # login(self.request, user)
        return redirect('login')


class UserUpdate(CustomUserPermisionsMixin, DataMixin, UpdateView):
    model = CustomUsers
    template_name = 'users/users_update.html'
    
    form_class = CustomUserCreationForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Редактирование")
        return context | c_def


class UserDelete(CheckUsersTasksMixin, CustomUserPermisionsMixin, DataMixin, DeleteView, LoginRequiredMixin):
    model = CustomUsers
    template_name = 'users/users_delete.html'
    success_url = reverse_lazy('users_list')
    context_object_name = "user"
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Удаление")
        return context | c_def

