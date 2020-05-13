from django.shortcuts import render
from .models import *
from Apps.users.models import *
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.


def forums(request):
    posts = Post.objects.all()
    preferences = Profile.objects.get(user=request.user)
    subforums = SubForum.objects.filter(category__profile__user=request.user)

    context = {
        'subforums': subforums,
        'posts': posts,
        'preferences': preferences,
    }
    return render(request, 'forums/main.html', context)


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'forums/main.html'


class SubforumList(ListView):
    model = SubForum
    context_object_name = 'subforums'
    template_name = 'forums/main.html'


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = '/task-tracker/home'
    fields = ['title', 'description', 'sub_forum']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/forums/'

    def test_func(self):
        return True
