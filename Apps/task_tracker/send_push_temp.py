"""Temp code for push notifications.

To be added to views.py"""
from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json

from task.models import Task
import datetime
import sched
import time


@login_required
@require_GET
def home(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
    else:
        form = TaskForm()

    context = {
        'form': form
    }

    return render(request, 'task_tracker/home.html', context)


@require_POST
@csrf_exempt
def send_push(request):
    try:
        body = request.body
        data = json.loads(body)

        if 'head' not in data or 'body' not in data or 'id' not in data:
            return JsonResponse(status=400, data={"message": "Invalid data format"})

        user = get_object_or_404(Task.user, pk=1)
        payload = {'head': Task.task_title, 'body': Task.description}
        push_notification = send_user_notification(user=user, payload=payload, ttl=1000)

        schedule = sched.scheduler(time.localtime, time.sleep)
        schedule.enterabs(time.strptime(Task.start_time), 0, push_notification)
        schedule.run()
        return JsonResponse(status=200, data={"message": "Web push successful"})

    except TypeError:
        return JsonResponse(status=500, data={"message": "An error occurred"})
