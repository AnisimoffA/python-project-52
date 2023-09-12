from django import forms
from task_manager.statuses.models import Status
from django.utils.translation import gettext as _


class StatusForm(forms.ModelForm):
    name = forms.CharField(
        label=_('Name'),
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = Status
        fields = ['name']
