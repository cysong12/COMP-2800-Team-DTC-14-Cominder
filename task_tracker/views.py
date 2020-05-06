from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {'tasks': Task.objects.all()
               }
    return render(request, 'task_tracker/home.html', context)


def about(request):
    return render(request, 'task_tracker/about.html', {'title': 'About us'})


def landing_page(request):
    return render(request, 'task_tracker/landing_page.html')


def contact(request):
    return render(request, 'task_tracker/contact.html')
