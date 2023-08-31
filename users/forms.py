from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUsers


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label="Имя", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Фамилия", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUsers
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']