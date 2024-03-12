from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
# from django.shortcuts import render
from ludic_language.todo.models import Task
from ludic_language.todo.forms import TaskCreateForm


class TodoListAddView(LoginRequiredMixin, CreateView):
    template = 'task_form.html'
    model = Task
    form_class = TaskCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['therapist'] = self.request.user.profile
        return kwargs

    def get_success_url(self):
        return reverse('index_speech')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'the task was created successfully')
        return super(TodoListAddView, self).form_valid(form)


class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('index_speech')
    form_class = TaskCreateForm

    def form_valid(self, form):
        messages.success(self.request, 'The Task was updated successfully.')
        return super(TodoUpdate, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['therapist'] = self.request.user.profile
        return kwargs


class TodoDetail(LoginRequiredMixin, DetailView):
    template_name = 'task_detail.html'
    model = Task
    context_object_name = 'task'


class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Task

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        result = HttpResponse(status=204)
        result["HX-Redirect"] = reverse_lazy('task_list')
        messages.success(self.request, 'The Task was deleted successfully.')
        return result

