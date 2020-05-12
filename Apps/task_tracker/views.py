from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


@login_required
def home(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'task_tracker/home.html', context)


def create_task(request):
    Task.objects.all().delete()
    test = Task.objects.create(title="Jog", description="Go for a jog", category="SPORTS")
    test.save()
    test = Task.objects.create(title="Cooking", description="Go cook something", category="COOK")
    test.save()
    test = Task.objects.create(title="Game", description="Go play games", category="GAMES")
    test.save()
    built_in_tasks = Task.objects.all()
    context = {
        'tasks': built_in_tasks
    }
    return render(request, 'task_tracker/create_task.html', context)


def generate_built_in_tasks():
    built_in_tasks = None
    pass


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    success_url = '/task-tracker/home'
    fields = ['title', 'description', 'date_start']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    success_url = '/task-tracker/home'
    fields = ['title', 'description', 'date_start']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/task-tracker/home'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


def about(request):
    return render(request, 'task_tracker/about.html', {'title': 'About us'})


def landing_page(request):
    return render(request, 'main/landing_page.html')


def contact(request):
    return render(request, 'main/contact.html')
