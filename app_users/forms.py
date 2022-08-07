from datetime import datetime
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationUserForm(UserCreationForm):
    """форма регистрации пользователя"""
    username = forms.CharField(max_length=30, label="Login name", widget=forms.TextInput(attrs={'class': "form-input"}))
    first_name = forms.CharField(max_length=30, label="Name", required=False,
                                 widget=forms.TextInput(attrs={'class': "form-input"}))
    last_name = forms.CharField(max_length=30, label="Last_name", required=False,
                                widget=forms.TextInput(attrs={'class': "form-input"}))
    fathers_name = forms.CharField(max_length=30, label="Fathers_name", required=False,
                                   widget=forms.TextInput(attrs={'class': "form-input"}))
    birthday = forms.DateField(widget=forms.widgets.SelectDateWidget(years=range(1999, datetime.now().year)),
                               required=False,
                               label='You`r birthday:')

    email = forms.EmailField(max_length=50, label="Email", widget=forms.TextInput(attrs={'class': "form-input"}))
    file = forms.FileField(label="Add Photo", required=False)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': "form-input"}))
    password2 = forms.CharField(label="Again Password", widget=forms.PasswordInput(attrs={'class': "form-input"}))

    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'fathers_name', 'birthday', 'username', 'email', 'file', 'password1',
            'password2')


class LoginUserForm(AuthenticationForm):
    """форма футентификации"""
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs={'class': "form-input"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': "form-input"}))

