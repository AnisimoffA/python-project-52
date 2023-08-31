from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.utils.translation import gettext as _
from task_manager.utils import *
from task_manager.forms import *

class MainPage(DataMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Менеджер задач Hexlet")
        return context | c_def

# - удалить

def test(request):
    return reverse('users_update', 7)

# - 
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "login_form.html"
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Вход")
        return context | c_def
    
    def get_success_url(self) -> str:
        return reverse_lazy('main_page')


def logout_user(request):
    logout(request)
    return redirect('main_page')
    
    
