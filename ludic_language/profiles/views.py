from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from . import forms


class LoginViewPatient(View):

    """Class Based View for patient user's login

    Attributes:
        template_name (str): template location
    """

    template_name = "authentication/login_patient.html"
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],)
            if user is not None:
                login(request, user)
                return redirect('index')
        message = 'Login Failed'
        return render(request, self.template_name, context={'form': form, 'message': message})


class LoginViewSpeech(View):
    """Class Based View for patient user's login

    Attributes:
        template_name (str): template location
    """
    template_name = "authentication/login_speech.html"
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],)
            if user is not None:
                login(request, user)
                return redirect('index_speech.html')
        message = 'Login Failed'
        return render(request, self.template_name, context={'form': form, 'message': message})
