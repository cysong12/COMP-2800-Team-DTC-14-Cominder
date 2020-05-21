from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Apps.task_tracker.models import *
from Apps.forums.models import *
from Apps.users.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from datetime import datetime
from django.db.models import Q, F
from django.db.models import Model
from django.views.decorators.csrf import csrf_exempt


@login_required
def home(request):
    username = None
    day_now = datetime.now()
    tasks = Task.objects.filter(Q(user=request.user) & Q(completed=False))
    if request.user.is_authenticated:
        username = request.user.username

    forums = SubForum.objects.filter(category__profile__user=request.user)
    posts = Post.objects.filter(sub_forum__in=forums)
    return_list = []
    for post in posts:
        return_list.append((post, post.likes.filter(id=request.user.id).exists()))

    context = {
        'username': username,
        'tasks': tasks,
        'posts': return_list,
    }
    return render(request, 'main/home.html', context)


class TaskListView(ListView):
    model = Task
    template_name = 'main/home.html'
    context_object_name = 'tasks'
    ordering = ['date_posted']


class TaskDetailView(DetailView):
    model = Task


def about(request):
    return render(request, 'main/about.html', {'title': 'About us'})


def landing_page(request):
    return render(request, 'main/landing_page.html')


def contact(request):
    return render(request, 'main/contact.html')


def social_share(request):
    return render(request, 'main/social_share.html')

