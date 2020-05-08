from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from django.contrib.auth.models import User


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
    try:
        tasks = Task.objects.filter(username='admin')
    except Exception as e:
        print(e)
    context = {
        'form': form,
        'task': task,
        # 'tasks': tasks,
    }

    return render(request, 'task_tracker/home.html', context)


def about(request):
    return render(request, 'task_tracker/about.html', {'title': 'About us'})


def landing_page(request):
    return render(request, 'main/landing_page.html')


def contact(request):
    return render(request, 'main/contact.html')
