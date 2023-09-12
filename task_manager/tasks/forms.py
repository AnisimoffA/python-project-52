from django import forms
from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from task_manager.users.models import CustomUsers
from task_manager.statuses.models import Status
from django.utils.translation import gettext as _


class TaskForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Name"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        label=_("Description"),
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    status = forms.ModelChoiceField(
        label=_("Status"),
        queryset=Status.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    executor = forms.ModelChoiceField(
        label=_("Executor"),
        required=False,
        queryset=CustomUsers.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    labels = forms.ModelMultipleChoiceField(
        label=_("Labels"),
        queryset=Label.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']


class FindTaskForm(forms. ModelForm):
    status = forms.ModelChoiceField(
        label=_("Status"),
        queryset=Status.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    executor = forms.ModelChoiceField(
        label=_("Executor"),
        required=False,
        queryset=CustomUsers.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    labels = forms.ModelChoiceField(
        label=_("Label"),
        queryset=Label.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )
    show_my_articles = forms.BooleanField(
        label=_("Show only my posts"),
        required=False
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
