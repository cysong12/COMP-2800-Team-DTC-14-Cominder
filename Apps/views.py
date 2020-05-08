from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Apps.task_tracker.models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from datetime import datetime
from django.db.models import Q


@login_required
def home(request):
    username = None
    day_now = datetime.now()
    tasks = Task.objects.filter(Q(date_start__day=day_now.day))
    if request.user.is_authenticated:
        username = request.user.username
    context = {
        'username': username,
        'tasks': tasks
    }
    return render(request, 'main/home.html', context)


class TaskListView(ListView):
    model = Task
    template_name = 'main/home.html'
    context_object_name = 'tasks'
    ordering = ['date_posted']

    def get_queryset(self):
        day_now = datetime.now()
        queryset = super(TaskListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class TaskDetailView(DetailView):
    model = Task


def about(request):
    return render(request, 'main/about.html', {'title': 'About us'})


def landing_page(request):
    return render(request, 'main/landing_page.html')


def contact(request):
    return render(request, 'main/contact.html')
