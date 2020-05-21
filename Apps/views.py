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


def update_points(user):
    profile_instance = Profile.objects.get(user=user)
    profile_instance.points = 0
    comments = Comment.objects.filter(posted_by=user)
    posts = Post.objects.filter(posted_by=user)
    for comment in comments:
        profile_instance.points += comment.total_likes()
    for post in posts:
        profile_instance.points += post.total_likes()
    profile_instance.save()


@login_required
def home(request):
    username = None
    day_now = datetime.now()
    tasks = Task.objects.filter(Q(user=request.user) & Q(completed=False))
    if request.user.is_authenticated:
        username = request.user.username

    forums = SubForum.objects.filter(category__profile__user=request.user)
    posts = Post.objects.filter(sub_forum__in=forums)
    # update_points(request.user)
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

def social_share(request):
    return render(request, 'main/social_share.html')

