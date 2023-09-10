from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.contrib import messages
from task_manager.utils import DataMixin
from task_manager.forms import LoginUserForm


class MainPage(DataMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_("Task manager Hexlet"))
        return context | c_def


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "login_form.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_("Login"))
        return context | c_def

    def get_success_url(self):
        messages.success(self.request, _("You are successfully logged in"))
        return reverse_lazy('main_page')


def logout_user(request):
    logout(request)
    messages.info(request, _("You are successfully logged out"))
    return redirect('main_page')
