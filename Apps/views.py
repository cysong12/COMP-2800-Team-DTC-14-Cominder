from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from Apps.task_tracker.models import *
from Apps.forums.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from datetime import datetime
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


@login_required
def home(request):
    username = None
    day_now = datetime.now()
    tasks = Task.objects.filter(Q(date_start__day=day_now.day) & Q(user=request.user))
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


def clicked_like(request):
    if request.POST:
        liked_post_id = request.POST.get()
        post = Post.objects.get(id=liked_post_id)
        post.likes += 1
        post.save(update_fields=["likes"])


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
