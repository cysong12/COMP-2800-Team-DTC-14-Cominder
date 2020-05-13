from django.shortcuts import render
from .models import *
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


def forums(request):
    subforums = SubForum.objects.all()
    posts = Post.objects.all()
    context = {
        'subforums': subforums,
        'posts': posts,
    }
    return render(request, 'forums/main.html', context)


class PostList(ListView):
    model = SubForum
    context_object_name = 'subforums'
    template_name = 'forums/main.html'


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    pass


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/forums/home'

    def test_func(self):
        return True
