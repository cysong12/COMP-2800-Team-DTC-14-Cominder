from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import *
from django.http import HttpResponseRedirect
from django.db.models import Q

from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json

import datetime
import sched
import time


@login_required
def home(request):
    tasks = Task.objects.filter(Q(completed=False))
    categories = Category.objects.all()
    context = {
        'tasks': tasks,
        'categories': categories,
    }
    return render(request, 'task_tracker/home.html', context)


def task_complete_form_to_creating_post(request, form_response):
    post_created = Post.objects.create(title=form_response['title'], posted_by=request.user,
                                       description=form_response['description'], sub_forum=form_response['sub_forum'],
                                       media=form_response['media'])
    post_created.save()
    return post_created


def complete(request, pk):
    task_instance = get_object_or_404(Task, pk=pk)
    post_created = ''
    if request.method == "POST":
        form = TaskCompleteForm(request.POST, request.FILES)
        if form.is_valid():
            form_response = form.cleaned_data
            post_created = task_complete_form_to_creating_post(request, form_response)
            task_instance.completed = True
            task_instance.save(update_fields=["completed"])
            return redirect('post-detail', pk=post_created.pk)
    else:
        form = TaskCompleteForm()
    context = {
        'form': form,
        'task': task_instance,
    }

    return render(request, 'task_tracker/task_complete.html', context)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    success_url = '/task-tracker/home'
    fields = ['title', 'category', 'description', 'date_start']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.fields['category'] = Category.category
        return super().form_valid(form)


class TaskDetailView(DetailView):
    model = Task


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    success_url = '/task-tracker/home'
    fields = ['title', 'description', 'date_start']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/task-tracker/home'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


def about(request):
    return render(request, 'task_tracker/about.html', {'title': 'About us'})


def landing_page(request):
    return render(request, 'main/landing_page.html')


def contact(request):
    return render(request, 'main/contact.html')


@login_required
@csrf_exempt
def send_push(request):
    try:
        body = request.body
        data = json.loads(body)

        if 'head' not in data or 'body' not in data or 'id' not in data:
            return JsonResponse(status=400, data={"message": "Invalid data format"})

        user = get_object_or_404(Task.user, pk=1)
        payload = {'head': Task.title, 'body': Task.description}
        push_notification = send_user_notification(user=user, payload=payload, ttl=1000)

        schedule = sched.scheduler(time.localtime, time.sleep)
        schedule.enterabs(time.strptime(Task.start_time), 0, push_notification)
        schedule.run()
        return JsonResponse(status=200, data={"message": "Web push successful"})

    except TypeError:
        return JsonResponse(status=500, data={"message": "An error occurred"})
