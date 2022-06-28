from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='пароль', widget=forms.TextInput(attrs={'class': 'form-control'}))