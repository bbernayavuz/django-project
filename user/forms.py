from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta():
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta():
        fields = [
            'username',
            'password'
        ]