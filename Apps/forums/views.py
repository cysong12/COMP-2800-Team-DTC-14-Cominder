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


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'forums/main.html'


class SubforumPostsList(ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'
    template_name = 'forums/subforum_main.html'

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(Q(sub_forum__pk=self.kwargs['pk']))


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
