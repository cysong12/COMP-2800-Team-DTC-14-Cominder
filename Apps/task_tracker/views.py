from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import *


@login_required
def home(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    context = {
        'tasks': tasks,
        'categories': categories,
    }
    return render(request, 'task_tracker/home.html', context)


def complete(request, pk):
    return render(request, 'task_tracker/task_complete.html')


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    success_url = '/task-tracker/home'
    fields = ['title', 'category', 'description', 'date_start']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.fields['category'] = Category.category
        return super().form_valid(form)


class TaskDetailView(DetailView):
    model = Task


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
