from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUsers
from django.utils.translation import gettext as _


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label=_("First name"),
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label=_("Last name"),
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        label=_("username"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUsers
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            # Проверяем уникальность username, исключая текущего пользователя
            CustomUsers.objects.exclude(
                username=username).get(username=username
                                       )
            raise forms.ValidationError(
                'Пользователь с таким именем уже существует.'
            )
        except CustomUsers.DoesNotExist:
            return username
