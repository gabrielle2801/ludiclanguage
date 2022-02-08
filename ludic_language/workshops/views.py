from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from ludic_language.workshops.models import Workshop
from ludic_language.workshops.forms import WorkshopForm


class WorkshopAddView(LoginRequiredMixin, CreateView):
    form_class = WorkshopForm
    model = Workshop
    template_name = 'form_workshop.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['therapist'] = self.request.user.profile
        return kwargs

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('list_workshop')
