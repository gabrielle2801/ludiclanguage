from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.template.loader import  render_to_string
from django.template import Context
import os
from dotenv import load_dotenv, find_dotenv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView


from django.views.generic.edit import UpdateView
import datetime
from ludic_language.profiles.models import User
from ludic_language.workshops.models import Workshop
from ludic_language.workshops.forms import WorkshopForm, ReportForm
load_dotenv(find_dotenv())

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
    
    def get_context_data(self, **kwargs):
        context_data = super(WorkshopUpdateView, self).get_context_data(**kwargs)
        workshop_obj = Workshop.objects.get(id=self.kwargs.get('pk'))
        user_id=workshop_obj.patient_id
        user_obj=User.objects.get(id=user_id)
        context_data['first_name'] = user_obj.first_name
        context_data['last_name'] = user_obj.last_name
        return context_data


    def form_valid(self, form, **kwargs):
        first_name = self.request.user.first_name
        last_name = self.request.user.last_name
        context_data = self.get_context_data(form=form, **kwargs)
        first_name = context_data['first_name']
        last_name = context_data['last_name']
        recievers = []
        for user in User.objects.exclude(email=self.request.user.email):
            recievers.append(user.email)
            recipient_list = recievers
        send_mail(
            'mise à jour',
                render_to_string('../templates/email.html',{
                    'first_name': first_name,
                    'last_name':last_name,
                    'patient': first_name,
                    'patient_name' : last_name
                }),
            self.request.user.email,
            recipient_list
        )
        return super().form_valid(form)
    
    
        
   
class ReportListView(ListView):
    template_name = 'report_list.html'
    model = Workshop
    context_object_name = 'report_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Workshop.objects.filter(
            patient_id=self.request.user.profile)\
            .order_by('-date')
        return queryset
    



class ReportDetailView(DetailView):
    model = Workshop
    template_name = 'report_patient.html'
    context_object_name = 'report'

