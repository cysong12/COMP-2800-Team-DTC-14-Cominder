from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from Apps.users.models import *
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q, F
from django.http import HttpResponse, JsonResponse
# Create your views here.


def forums(request):
    # posts = Post.objects.all()
    preferences = Profile.objects.get(user=request.user)
    forums = SubForum.objects.filter(category__profile__user=request.user)
    posts = Post.objects.filter(sub_forum__in=forums)

    context = {
        'forums': forums,
        'posts': posts,
        'preferences': preferences,
    }
    return render(request, 'forums/main.html', context)


def subforum_posts(request, pk):
    post_instances = Post.objects.filter(sub_forum__pk=pk)
    context = {
        'posts': post_instances,
    }
    return render(request, 'forums/main.html', context)


def increment_like(request):
    if request.method == 'GET':
        user = request.user     # associate users' likes with post so no dupes; modify models
        pk = request.GET['post_pk']
        post_instance = Post.objects.filter(pk=pk).update(likes=F('likes') + 1)
        post_instance.save()
        # return JsonResponse({'likes': post_instance.likes})
        return HttpResponse("Success")
    else:
        # return JsonResponse({'likes': "request method is not GET"})
        return HttpResponse("Got to be GET")


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'forums/main.html'


class SubforumList(ListView):
    model = SubForum
    context_object_name = 'forums'
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
