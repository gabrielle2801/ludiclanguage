from django.views.generic import DetailView
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.urls import reverse_lazy
# from collections import defaultdict

from ludic_language.exercises.models import Pathology, LudicJourney, Exercise
from ludic_language.exercises.forms import LudicJourneyCreateForm, LudicJourneyAssessementForm


class PathologyDetailView(DetailView):
    model = Pathology
    template_name = 'pathology.html'
    context_object_name = 'pathology_des'

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(pk=self.request.user.profile.pathology_id)
        return qs


class ExerciseListView(LoginRequiredMixin, ListView):
    template_name = 'exercise_list.html'
    context_object_name = 'pathology_list'
    model = Pathology

    def get_queryset(self):
        qs = super().get_queryset()
        qs.select_related('exercise')
        return qs


class LudicJourneyAddView(LoginRequiredMixin, CreateView):
    form_class = LudicJourneyCreateForm
    model = LudicJourney
    template_name = 'form_ludicjourney.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['therapist'] = self.request.user.profile
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['exercise'] = self.kwargs.get('exercise_id')
        return initial

    def get_success_url(self):
        return reverse('exercise_list')


class LudicJouneyListView(LoginRequiredMixin, ListView):
    template_name = 'ludic_journey.html'
    model = LudicJourney
    context_object_name = 'ludicjourney_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            patient_id=self.request.user.profile.user_id)
        return queryset


class LudicJouneyListTherapistView(LoginRequiredMixin, ListView):
    template_name = 'exercise_therapist.html'
    model = LudicJourney
    context_object_name = 'exercise_therapist'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('exercise')
        return queryset


class LudicJourneyDetailView(LoginRequiredMixin, DetailView):
    template_name = 'play_on.html'
    model = Exercise
    context_object_name = 'exercise_detail'


class LudicJourneyUpdateView(LoginRequiredMixin, UpdateView):
    model = LudicJourney
    form_class = LudicJourneyAssessementForm
    template_name = 'form_assessement.html'
    success_url = reverse_lazy('exercise_therapist')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['patient'] = self.request.user.profile
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['exercise'] = self.kwargs.get('ludicjourney_id')
        return initial

    def get_success_url(self):
        return reverse('exercise_list')


class AssessementDetailView(LoginRequiredMixin, DetailView):
    model = LudicJourney
    template_name = 'assessement.html'
    context_object_name = 'assessement'


'''
-- Django version --
 class ExerciseListView(LoginRequiredMixin, ListView):
    template_name = 'exercise_list.html'
    context_object_name = 'pathology_list'
    model = Pathology

    def get_queryset(self):
        qs = super().get_queryset()
        qs.select_related('exercise')
        return qs

-- Python version --
class ExerciseListView(LoginRequiredMixin, ListView):
    template_name = 'exercise_list.html'
    context_object_name = 'exercise_list'
    model = Exercise

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        exercises = context['exercise_list']
        pathologies = defaultdict(list)
        for exercise in exercises:
            pathologies[exercise.pathology.name].append(exercise)
        path = sorted(pathologies.items())
        # sorted(pathologies.items())
        context['pathologies'] = path
        return context
'''
