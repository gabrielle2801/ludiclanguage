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
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)


class ProfileForm(forms.ModelForm):

    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        try:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
        except User.DoesNotExist:
            pass

    class Meta:
        model = Profile
        fields = ('birth_date', 'bio', 'profile_pic', 'pathology')


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
