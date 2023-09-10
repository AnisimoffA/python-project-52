from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from task_manager.utils import * # NOQA F403
from users.forms import * # NOQA F403
from users.models import * # NOQA F403


class UserList(DataMixin, ListView):
    model = CustomUsers
    template_name = "users/users_list.html"
    context_object_name = "users"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_("Users"))
        return context | c_def

    def get_queryset(self):
        return CustomUsers.objects.all()


class UserRegister(DataMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = "register_form.html"
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_("Registration"))
        return context | c_def

    def form_valid(self, form):
        messages.success(self.request, _("You have successfully registered"))
        form.save()
        return redirect('login')


class UserUpdate(CustomUserPermisionsMixin, DataMixin, UpdateView):
    model = CustomUsers
    template_name = 'users/users_update.html'

    form_class = CustomUserCreationForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_("Updating user"))
        return context | c_def

    def get_success_url(self):
        messages.success(
            self.request,
            _("User was updated successfully")
        )
        return reverse_lazy('users_list')


class UserDelete(CheckUsersTasksMixin, DataMixin, DeleteView, LoginRequiredMixin): # NOQA E501
    model = CustomUsers
    template_name = 'users/users_delete.html'
    success_url = reverse_lazy('users_list')
    context_object_name = "user"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_("Deleting"))
        return context | c_def

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        messages.success(self.request, _("User was deleted successfully"))
        return response
