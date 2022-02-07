from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from ludic_language.workshops.models import Workshop
from ludic_language.workshops.forms import WorkshopForm


class PatientAddView(LoginRequiredMixin, CreateView):
    form_class = WorkshopForm
    model = Workshop
    template_name = 'form_workshop.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['patient'] = self.user.profile
        return kwargs

    def get_success_url(self):
        return reverse('list_workshop')
