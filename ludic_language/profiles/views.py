from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from ludic_language.profiles.models import STATES
from . import forms

from ludic_language.profiles.models import User
from ludic_language.profiles.forms import PatientForm, AddressForm


class LoginView(BaseLoginView):

    """Class Based View for patient user's login

    Attributes:
        template_name (str): template location
    """

    template_name = "authentication/login.html"

    def get_success_url(self):
        user = self.request.user
        if user.state == STATES.PATIENT:
            return reverse('index_patient')
        else:
            return reverse('index_speech')


def logout_request(request):
    """ function to logout

    Args:
        request (TYPE): HTTpRequest request to generate a answer

    Returns:
        TYPE: redirect to base.html
    """
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')


class IndexSpeechView(TemplateView):
    template_name = "index_speech.html"


class IndexPatientView(TemplateView):
    template_name = "index_patient.html"


class PatientListView(ListView):
    template_name = 'patient_list.html'
    model = User


class PatientView(View):
    form_class = PatientForm
    form_ad = AddressForm
    template_name = "form_patient.html"

    def get(self, request, *args, **kwargs):
        """Summary

        Args:
            request (TYPE): HTTpRequest request to generate a answer
            *args: Description
            **kwargs: Description

        Returns:
            TYPE: HttpResponse object with template name and form information
        """
        form = self.form_class()
        form2 = self.form_ad()
        context = {
            'form': form,
            'form2': form2
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        """Form to login for user's account
        save users's information on database if form is valid
        on Class Based View
        class SignUpView(CreateView):
            form_class = UserCreationForm
            success_url = reverse_lazy('base')
            template_name = 'registration/sign_up.html'

        Args:
            request (TYPE): HTTpRequest request to generate a answer
            *args: Description
            **kwargs: Description

        Returns:
            TYPE: HttpResponse object with template name and form information
        """
        form = self.form_class(data=request.POST)
        form2 = self.form_ad(data=request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index_speech')
        if form2.is_valid():
            form2.save()

        context = {
            'form': form,
            'form2': form2
        }
        return render(request, self.template_name, context=context)
