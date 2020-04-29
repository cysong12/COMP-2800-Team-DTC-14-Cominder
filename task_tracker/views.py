from django.shortcuts import render
from .models import Task

def home(request):
    context = {'tasks': Task.objects.all()
	}
    return render(request, 'task_tracker/home.html', context)

def about(request):
	return render(request, 'task_tracker/about.html', {'title': 'About us'})
