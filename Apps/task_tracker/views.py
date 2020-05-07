from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import TaskForm


@login_required
def home(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, 'main/home.html', context)

class TaskListView(ListView):
    model = Task
    template_name = 'main/home.html'
    context_object_name = 'tasks'
    ordering = ['-date_posted']


def about(request):
    return render(request, 'main/about.html', {'title': 'About us'})


def landing_page(request):
    return render(request, 'main/landing_page.html')


def contact(request):
    return render(request, 'main/contact.html')
