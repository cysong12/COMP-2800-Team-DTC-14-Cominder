from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Apps.task_tracker.models import CustomTask
from Apps.forums.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from datetime import datetime
from django.db.models import Q


@login_required
def home(request):
    username = None
    day_now = datetime.now()
    tasks = CustomTask.objects.filter(Q(date_start__day=day_now.day) & Q(user=request.user))
    if request.user.is_authenticated:
        username = request.user.username
    posts = Post.objects.all()
    context = {
        'username': username,
        'tasks': tasks,
        'test1': 'hello',
        'posts': posts,
    }
    return render(request, 'main/home.html', context)


class CustomTaskListView(ListView):
    model = CustomTask
    template_name = 'main/home.html'
    context_object_name = 'tasks'
    ordering = ['date_posted']


'''
    def get_queryset(self):
        queryset = super(TaskListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
'''


class CustomTaskDetailView(DetailView):
    model = CustomTask


def about(request):
    return render(request, 'main/about.html', {'title': 'About us'})


def landing_page(request):
    return render(request, 'main/landing_page.html')


def contact(request):
    return render(request, 'main/contact.html')
