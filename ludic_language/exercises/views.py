from django.views.generic import DetailView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# from collections import defaultdict
from ludic_language.exercises.models import Pathology, Exercise


class PathologyDetailView(DetailView):
    model = Pathology
    template_name = 'pathology.html'
    context_object_name = 'pathology_des'


class ExerciseListView(LoginRequiredMixin, ListView):
    template_name = 'exercise_list.html'
    context_object_name = 'pathology_list'
    model = Pathology

    def get_queryset(self):
        qs = super().get_queryset()
        qs.select_related('exercise')
        return qs


'''
 result = [{'type': k, 'items': [x[0] for x in v]} for k, v in groups]
        print(result)
        pathologies[exercise.pathology.name] = [exercise]

def get_context_data(self, **kwargs):
        context = super().get_context_data()
        pathologies = {}
        exercises = context['exercise_list']
        for exercise in exercises:
            pathologies[exercise] = [exercise.pathology.name]
            pathology = groupby(
                pathologies, lambda pathology: [exercise.pathology.name])
        print(pathologies)
        context['pathologies'] = pathologies
        return context


 for exercise in exercises:
            pathologies[exercise.pathology.name].append(exercise)
            [{'pathology_name': pathology, 'exercises': exercise}
                for pathology, exercises in pathologies.items()]
        context['pathologies'] = dict(pathologies)
        print(pathologies)
        return context

    pathologies_list = [{'pathology_name': exercise.pathology.name, 'exercises': exercise}
                                for exercise.pathology.name, exercises in pathologies.items()]
'''
