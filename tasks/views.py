from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView # NOQA E501
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.contrib import messages
from django.urls import reverse_lazy
from tasks.forms import FindTaskForm, TaskForm
from task_manager.utils import DataMixin, CustomTaskPermisionsMixin
from users.models import CustomUsers
from tasks.models import Task


class TaskList(LoginRequiredMixin, DataMixin, ListView):
    model = Task
    template_name = "tasks/task_list.html"
    login_url = reverse_lazy("login")
    context_object_name = "tasks"
    form_class = FindTaskForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_("Tasks"))
        context['form'] = self.form_class(self.request.GET)

        return context | c_def

    def get_queryset(self):
        queryset = Task.objects.all()
        form = self.form_class(self.request.GET)

        # Фильтруем queryset на основе данных из формы поиска
        if form.is_valid():
            status = form.cleaned_data.get('status')
            executor = form.cleaned_data.get('executor')
            labels = form.cleaned_data.get('labels')
            show_my_articles = form.cleaned_data.get('show_my_articles')

            if status:
                queryset = queryset.filter(status=status)
            if executor:
                queryset = queryset.filter(executor=executor)
            if labels:
                queryset = queryset.filter(labels=labels)
            if show_my_articles:
                queryset = queryset.filter(creator=self.request.user)

        return queryset


class TaskPage(LoginRequiredMixin, DataMixin, DetailView):
    model = Task
    template_name = "tasks/task_page.html"
    context_object_name = 'task'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_("Task page"))
        return context | c_def


class TaskCreate(LoginRequiredMixin, DataMixin, CreateView):
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    login_url = reverse_lazy('login')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_("Task creating"))
        return context | c_def

    def form_valid(self, form):
        current_user_id = self.request.user.id
        form.instance.creator = CustomUsers.objects.get(id=current_user_id)
        super().form_valid(form)
        messages.success(self.request, _("Task was successfully created"))
        return redirect('task_list')


class TaskUpdate(LoginRequiredMixin, DataMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_("Task updating"))
        return context | c_def

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _("Task was successfully updated"))
        return redirect('task_list')


class TaskDelete(CustomTaskPermisionsMixin, LoginRequiredMixin, DataMixin, DeleteView): # NOQA E501
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task_list')
    context_object_name = "task"
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_("Task deleting"))
        return context | c_def

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(
                self.request,
                _("Task was successfully deleted")
            )
            return response
        except Exception:
            messages.warning(
                self.request,
                _("Only the author can delete the task")
            )
            return HttpResponseRedirect(reverse_lazy('statuses_list'))
