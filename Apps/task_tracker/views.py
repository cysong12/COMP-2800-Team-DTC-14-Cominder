from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CustomTask, BuiltInTask
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


@login_required
def home(request):
    tasks = CustomTask.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'task_tracker/home.html', context)


def create_task(request):
    BuiltInTask.objects.all().delete()
    test = BuiltInTask.objects.create(title="Jog", description="Go for a jog", category="SPORTS")
    test.save()
    test = BuiltInTask.objects.create(title="Cooking", description="Go cook something", category="COOK")
    test.save()
    test = BuiltInTask.objects.create(title="Game", description="Go play games", category="GAMES")
    test.save()
    built_in_tasks = BuiltInTask.objects.all()
    context = {
        'tasks': built_in_tasks
    }
    return render(request, 'task_tracker/create_task.html', context)


def generate_built_in_tasks():
    built_in_tasks = None
    pass


class CustomTaskDetailView(DetailView):
    model = CustomTask


class CustomTaskCreateView(LoginRequiredMixin, CreateView):
    model = CustomTask
    success_url = '/task-tracker/home'
    fields = ['title', 'description', 'date_start']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CustomTaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomTask
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


class CustomTaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CustomTask
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
