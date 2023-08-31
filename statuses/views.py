from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from task_manager.utils import *

# Create your views here.
class StatusesList(LoginRequiredMixin, DataMixin, TemplateView): # не забыть поменять на ListView
    template_name = "statuses/statuses_list.html"
    login_url = reverse_lazy("login")
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Статусы")
        return context | c_def