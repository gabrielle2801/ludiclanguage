from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
# from django.contrib.auth.mixins import LoginRequiredMixin

from ludic_language.exercises.models import Pathology, Exercise


class PathologyDetailView(DetailView):
    model = Pathology
    template_name = 'pathology.html'
    context_object_name = 'pathology_des'


class ExerciseDetailView(SingleObjectMixin, ListView):
    template_name = 'exercise_list.html'
    context_object_name = 'exercise'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Pathology.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercises_list'] = self.object
        return context

    def get_queryset(self):
        return self.exercise_set.all()
