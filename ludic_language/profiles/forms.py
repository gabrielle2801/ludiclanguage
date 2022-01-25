from django import forms
# from .models import Address
from ludic_language.profiles.models import User, Profile
from django.contrib.auth.forms import UserCreationForm
# from betterforms.multiform import MultiModelForm
# from ludic_language.exercises.models import Pathology


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(required=True)

    class meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']


class ProfileForm(forms.ModelForm):

    therapist = forms.ModelChoiceField(
        queryset=Profile.objects.all())

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            therapist = self.fields['therapist']
            therapist.queryset = therapist.queryset.filter(user=user)

    class Meta:
        model = Profile
        fields = ('birth_date', 'bio', 'profile_pic', 'pathology', 'therapist')


'''
class AddressForm(forms.ModelForm):
    num = forms.IntegerField()
    street = forms.CharField()
    zip_code = forms.CharField()
    city = forms.CharField()

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].queryset = Address.objects.filter(user=user)

    class Meta:
        model = Address
        fields = ['num', 'street', 'zip_code', 'city']
'''
