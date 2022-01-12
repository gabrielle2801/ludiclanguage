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


class LoginView(BaseLoginView):

    """Class Based View for patient user's login

    Attributes:
        template_name (str): template location
    """

    template_name = "authentication/login.html"

    def get_success_url(self):
        user = self.request.user
        if user.state == STATES.PATIENT:
            return reverse()
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


class PatientListView(ListView):
    template_name = 'patient_list.html'
    model = User


'''
class SpeechTherapistListView(ListView):
    template_name = ''
    model = User
'''
