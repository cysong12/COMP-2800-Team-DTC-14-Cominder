from django.contrib import messages
from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm


@login_required
def home(request):
    task = ''
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            task = form.save()
        else:
            messages.error(request, "Please correct the errors marked in red.")
    else:
        form = TaskForm()

    context = {
        'form': form,
        'task': task
    }

    return render(request, 'task_tracker/home.html', context)


def about(request):
    return render(request, 'task_tracker/about.html', {'title': 'About us'})


def landing_page(request):
    return render(request, 'main/landing_page.html')


def contact(request):
    return render(request, 'main/contact.html')
