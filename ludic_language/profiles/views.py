from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import redirect, reverse, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView
from django.views.generic.edit import DeleteView
from ludic_language.profiles.models import STATES
import datetime
from django.db.models import Q
from ludic_language.profiles.models import User, Profile
from ludic_language.exercises.models import Pathology
from ludic_language.workshops.models import Workshop
from ludic_language.todo.models import Task
from ludic_language.profiles.forms import UserProfileForm


class LoginView(BaseLoginView):

    """Class Based View for patient user's login

    Attributes:
        template_name (str): template location
    """

    template_name = "authentication/login.html"

    def get_success_url(self):
        user = self.request.user.profile
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
    model = User
    template_name = "index_speech.html"
   
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['workshop_date'] = Workshop.objects.filter(
            therapist_id=self.request.user.profile,
            date__date=datetime.date.today())
        context['task_date'] = Task.objects.all()
        return context


class IndexPatientView(TemplateView):
    template_name = "index_patient.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['workshop_date'] = Workshop.objects.filter(
            patient_id=self.request.user.profile,
            date__date=datetime.date.today())
        return context


class TherapistListView(ListView):
    template_name = 'therapist_list.html'
    model = Profile
    context_object_name = 'therapist_list'

    def get_queryset(self):
        search = self.request.GET.get('search_therapist', '').strip()
        queryset = super().get_queryset()
        if search:
            return queryset.filter(
                Q(address__city__icontains=search)
                | Q(address__zip_code__icontains=search), state=2)
        else:
            queryset


class PatientListView(ListView):
    template_name = 'patient_list.html'
    model = Profile
    context_object_name = 'patient_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Profile.objects.filter(
            therapist_id=self.request.user.profile)
        return queryset


class PatientAddView(LoginRequiredMixin, CreateView):
    form_class = UserProfileForm
    model = User
    template_name = 'form_patient.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['therapist'] = self.request.user.profile
        return kwargs

    def get_success_url(self):
        return reverse('index_speech')


class TherapistDetailView(DetailView):
    template_name = 'detail_therapist.html'
    model = Profile
    context_object_name = 'therapist'


class PatientDetailView(DetailView):
    template_name = 'detail_patient.html'
    model = Profile
    context_object_name = 'patient'


class PathologyDetailView(ListView):
    model = Pathology
    template_name = 'pathology.html'


class PatientDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete favorite product of the list
    Attributes:
        model (TYPE): Substitute model
        success_url (TYPE): url of favorite template if is ok
    """

    model = User
    context_object_name = 'patient_list'
    template_name = 'patient_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'La fiche patient a bien été supprimé')
        return reverse_lazy('patient_list')

    def page_not_found_view(request):
        return render(request, 'profiles/404.html')


def handle_server_error(request):
    return render(request, '500.html')
