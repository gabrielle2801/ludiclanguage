from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import redirect, reverse, render
from django.views.generic import CreateView, DetailView
from ludic_language.profiles.models import STATES
from django.http import HttpResponseRedirect
from ludic_language.profiles.models import User, Profile
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
    template_name = "index_speech.html"


class IndexPatientView(TemplateView):
    template_name = "index_patient.html"


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


class PatientDetailView(DetailView):
    template_name = 'detail_patient.html'
    model = Profile
    context_object_name = 'patient'


'''
class PatientAddView(LoginRequiredMixin, CreateView):
    form_class = UserForm
    second_form_class = ProfileForm
    template_name = 'form_patient.html'

    def get(self, request, *args, **kwargs):
        user_form = self.form_class()
        profile_form = self.second_form_class(user=request.user)
        context = {'user_form': user_form,
                   'profile_form': profile_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        user_form = self.form_class(data=request.POST)
        profile_form = self.second_form_class(
            request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('index_speech')




class PatientUpdateView(UpdateView):
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
    model = User
    template_name = 'form_patient.html'
    form_class = UserForm
    second_form_class = ProfileForm

    def get_context_data(self, **kwargs):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        user_form = UserForm(self.request.POST, instance=user)
        profile_form = ProfileForm(self.request.POST, instance=profile)
        context = super(PatientCreateView, self).get_context_data(**kwargs)
        context['forms'] = [user_form, profile_form]
        return context

    def get(self, request, *args, **kwargs):
        # super(PatientCreateView).get(request, *args, **kwargs)
        # user = self.request.user
        # profile = Profile.objects.get(user=user)
        user_form = self.form_class()
        profile_form = self.second_form_class()
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, self.template_name, context)

    def form_valid(self, form):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        user_form = UserForm(self.request.POST, instance=user)
        profile_form = ProfileForm(self.request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(self.request, "Your profile was updated.")
            return reverse('index_speech')

    def get_success_url(self):
        return reverse('index_speech')
'''
