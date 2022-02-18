from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView

from django.views.generic.edit import UpdateView
import datetime

from ludic_language.workshops.models import Workshop
from ludic_language.workshops.forms import WorkshopForm, ReportForm


class WorkshopAddView(LoginRequiredMixin, CreateView):
    form_class = WorkshopForm
    model = Workshop
    template_name = 'form_workshop.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['therapist'] = self.request.user.profile
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['patient'] = self.kwargs.get('patient_id')
        return initial

    def get_success_url(self):
        return reverse('list_workshop')


class WorkshopListView(ListView):
    template_name = 'list_workshop.html'
    model = Workshop
    context_object_name = 'list_workshop'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Workshop.objects.filter(
            therapist_id=self.request.user.profile)\
            .order_by('-date')
        return queryset


class WorkshopUpdateView(LoginRequiredMixin, UpdateView):
    model = Workshop
    form_class = ReportForm
    template_name = 'form_report.html'
    success_url = reverse_lazy('list_workshop')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['therapist'] = self.request.user.profile
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['patient'] = self.kwargs.get('patient_id')
        return initial


class ReportListView(ListView):
    template_name = 'report_list.html'
    model = Workshop
    context_object_name = 'report_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Workshop.objects.filter(
            patient_id=self.request.user.profile)\
            .filter(date__lte=datetime.date.today())
        return queryset


class ReportDetailView(DetailView):
    model = Workshop
    template_name = 'report_patient.html'
    context_object_name = 'report'
