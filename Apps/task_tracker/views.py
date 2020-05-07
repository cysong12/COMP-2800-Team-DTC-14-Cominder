from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm


@login_required
def home(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
    else:
        form = TaskForm()

    context = {
        'form': form
    }

    return render(request, 'task_tracker/home.html', context)


def about(request):
    return render(request, 'task_tracker/about.html', {'title': 'About us'})


def landing_page(request):
    return render(request, 'base/landing_page.html')


def contact(request):
    return render(request, 'base/contact.html')
