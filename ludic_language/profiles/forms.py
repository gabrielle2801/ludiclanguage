from django import forms
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    picture = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'password', 'picture']
