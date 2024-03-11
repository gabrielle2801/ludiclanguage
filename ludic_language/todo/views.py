from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# from django.views.decorators.http import require_http_methods
# from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
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


class TodoListView(ListView):
    model = Task
    template_name = "index_speech.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['task_list'] = Task.objects.filter(
            therapist_id=self.request.user.profile)\
            .order_by('-priority')
        return context


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
    template_name = "task_delete.html"
    model = Task
    success_url = reverse_lazy('index_speech')

    def form_valid(self, form):
        messages.success(self.request, 'The Task was deleted successfully.')
        return super(TodoDelete, self).form_valid(form)


'''
def deleteTask(request, pk):
    Task.objects.get(id=pk).delete()
    tasks = Task.objects.filter(therapist_id=request.user.id)
    context = {'task': tasks}
    return render(request, "todo/task_list.html", context)

class TodoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'tasks_list.html'
    model = Task
    success_url = reverse_lazy('index_speech')
    context_object_name = 'task'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['therapist'] = self.request.user.profile
        return kwargs

'''

