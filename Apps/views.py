from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Apps.task_tracker.models import Task


@login_required
def home(request):
    username = None
    tasks = Task.objects.filter()
    if request.user.is_authenticated:
        username = request.user.username
    context = {
        'username': username
    }
    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html', {'title': 'About us'})


def landing_page(request):
    return render(request, 'main/landing_page.html')


def contact(request):
    return render(request, 'main/contact.html')
