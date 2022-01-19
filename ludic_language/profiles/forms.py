from django import forms
from .models import User, Address


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    picture = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'password', 'picture']


class PatientForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    picture = forms.ImageField()
    email = forms.EmailField(required=True)
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'picture', 'email', 'bio']


class AddressForm(forms.Form):
    num = forms.IntegerField()
    street = forms.CharField()
    zip_code = forms.CharField()
    city = forms.CharField()

    class Meta:
        model = Address
        fields = ['num', 'street', 'zip_code', 'city']
