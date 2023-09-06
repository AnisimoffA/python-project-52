from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django import forms
from django.db.models import RestrictedError
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from task_manager.utils import *
from labels.models import Label
from labels.forms import LabelForm
# Create your views here.


class LabelsList(LoginRequiredMixin, DataMixin, ListView):
    model = Label
    template_name = "labels/labels_list.html"
    context_object_name = "labels"
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Метки")
        return context | c_def

    def get_queryset(self):
        return Label.objects.all()


class LabelCreate(LoginRequiredMixin, DataMixin, CreateView):
    form_class = LabelForm
    template_name = 'labels/label_create.html'
    login_url = reverse_lazy('login')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Статусы")
        return context | c_def

    def get_success_url(self):
        messages.success(self.request, "Метка успешно создана")
        return reverse_lazy('labels_list')


class LabelUpdate(LoginRequiredMixin, DataMixin, UpdateView):
    model = Label
    template_name = 'labels/label_update.html'
    login_url = reverse_lazy('login')

    form_class = LabelForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Редактирование")
        return context | c_def

    def get_success_url(self):
        messages.success(self.request, "Метка успешно изменена")
        return reverse_lazy('labels_list')


class LabelDelete(DeleteView, LoginRequiredMixin, DataMixin):
    model = Label
    template_name = 'labels/label_delete.html'
    context_object_name = "status"
    success_url = reverse_lazy('labels_list')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TEST Удаление")
        return context | c_def

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(self.request, "Метка успешно удалена")
            return response
        except RestrictedError:
            messages.warning(self.request, "Невозможно удалить метку, потому что она используется.")
            return HttpResponseRedirect(reverse_lazy('labels_list'))
