from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.db.models import RestrictedError
from task_manager.utils import *
from statuses.models import Status
from statuses.forms import StatusForm
# Create your views here.


class StatusesList(LoginRequiredMixin, DataMixin, ListView):
    model = Status
    template_name = "statuses/statuses_list.html"
    context_object_name = "statuses"
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Статусы")
        return context | c_def

    def get_queryset(self):
        return Status.objects.all()


class StatusesCreate(LoginRequiredMixin, DataMixin, CreateView):
    form_class = StatusForm
    template_name = 'statuses/statuses_create.html'
    login_url = reverse_lazy('login')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Статусы")
        return context | c_def
    
    def get_success_url(self):
        messages.success(self.request, "Статус успешно создан")
        return reverse_lazy('statuses_list')


class StatusesUpdate(LoginRequiredMixin, DataMixin, UpdateView):
    model = Status
    template_name = 'statuses/statuses_update.html'
    login_url = reverse_lazy('login')
    
    form_class = StatusForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Редактирование")
        return context | c_def

    def get_success_url(self):
        messages.success(self.request, "Статус успешно изменен")
        return reverse_lazy('statuses_list')


class StatusesDelete(DeleteView, LoginRequiredMixin, DataMixin):
    model = Status
    template_name = 'statuses/statuses_delete.html'
    context_object_name = "status"
    success_url = reverse_lazy('statuses_list')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Удаление")
        return context | c_def

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(self.request, "Статус успешно удален")
            return response
        except RestrictedError:
            messages.warning(self.request, "Невозможно удалить статус, потому что он используется.")
            return HttpResponseRedirect(reverse_lazy('statuses_list'))
