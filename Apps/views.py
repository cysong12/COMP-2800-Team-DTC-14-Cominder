from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Apps.task_tracker.models import *
from Apps.forums.models import *
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
    context = {
        'username': username,
        'tasks': tasks,
        'posts': posts,
    }
    return render(request, 'main/home.html', context)


'''
def increment_like(request, pk):
    post_instance = Post.objects.filter(pk=pk).update(likes=F('likes') + 1)
    return redirect('feature-home')'''


class TaskListView(ListView):
    model = Task
    template_name = 'main/home.html'
    context_object_name = 'tasks'
    ordering = ['date_posted']


'''
    def get_queryset(self):
        queryset = super(TaskListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
'''


class TaskDetailView(DetailView):
    model = Task


def about(request):
    return render(request, 'main/about.html', {'title': 'About us'})


def landing_page(request):
    return render(request, 'main/landing_page.html')


def contact(request):
    return render(request, 'main/contact.html')
