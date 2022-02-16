from django.views.generic import DetailView
from ludic_language.exercises.models import Pathology


class PathologyDetailView(DetailView):
    model = Pathology
    template_name = 'pathology.html'
    context_object_name = 'pathology_des'
