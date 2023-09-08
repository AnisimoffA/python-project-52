from django import forms
from labels.models import Label
from django.utils.translation import gettext as _


class LabelForm(forms.ModelForm):
    name = forms.CharField(
        label=_('Name'),
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = Label
        fields = ['name']
