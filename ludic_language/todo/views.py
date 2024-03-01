from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import  reverse
from ludic_language.todo.models import Task
from ludic_language.todo.forms import TaskCreateForm

# Create your views here.


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
    template = 'task_list.html'
    context_object_name = 'tasks'

    