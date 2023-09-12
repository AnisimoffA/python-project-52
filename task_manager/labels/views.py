from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import RestrictedError
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.utils import DataMixin
from django.contrib import messages
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from django.utils.translation import gettext as _


class LabelsList(LoginRequiredMixin, DataMixin, ListView):
    model = Label
    template_name = "labels/labels_list.html"
    context_object_name = "labels"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_("Labels"))
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
        c_def = self.get_user_context(title=_("Label creating"))
        return context | c_def

    def get_success_url(self):
        messages.success(
            self.request,
            _("Label was created successfully")
        )
        return reverse_lazy('labels_list')


class LabelUpdate(LoginRequiredMixin, DataMixin, UpdateView):
    model = Label
    template_name = 'labels/label_update.html'
    login_url = reverse_lazy('login')

    form_class = LabelForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_("Label updating"))
        return context | c_def

    def get_success_url(self):
        messages.success(self.request, _("Label was updated successfully"))
        return reverse_lazy('labels_list')


class LabelDelete(DeleteView, LoginRequiredMixin, DataMixin):
    model = Label
    template_name = 'labels/label_delete.html'
    context_object_name = "label"
    success_url = reverse_lazy('labels_list')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_("Label deleting"))
        return context | c_def

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(self.request, _("Label was deleted successfully"))
            return response
        except RestrictedError:
            messages.warning(
                self.request,
                _("It is not possible to delete the label because it is being used.") # NOQA E501
            )
            return HttpResponseRedirect(reverse_lazy('labels_list'))
