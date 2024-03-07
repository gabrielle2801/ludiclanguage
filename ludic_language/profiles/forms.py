from django import forms
from ludic_language.profiles.models import User, Address
from ludic_language.exercises.models import Pathology
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserProfileForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(required=True)
    birth_date = forms.DateField()
    bio = forms.CharField(widget=forms.Textarea)
    review = forms.CharField(widget=forms.Textarea)
    profile_pic = forms.ImageField(required=False)
    pathology = forms.ModelChoiceField(queryset=Pathology.objects.all())
    num = forms.IntegerField()
    street = forms.CharField()
    zip_code = forms.CharField()
    city = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']

    def __init__(self, *args, therapist=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.therapist = therapist

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        address = Address.objects.create(
            profile=user.profile, num=self.cleaned_data['num'], 
            street=self.cleaned_data['street'],
            zip_code=self.cleaned_data['zip_code'],
            city=self.cleaned_data['city'])
        user.profile.birth_date = self.cleaned_data['birth_date']
        user.profile.therapist = self.therapist
        user.profile.bio = self.cleaned_data['bio']
        user.profile.review = self.cleaned_data['review']
        user.profile.profile_pic = self.cleaned_data['profile_pic']
        user.profile.pathology = self.cleaned_data['pathology']
        user.profile.save()
        user.profile.address.save()
        return user
