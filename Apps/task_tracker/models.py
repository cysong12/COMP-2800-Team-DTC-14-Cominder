from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Tasks(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=None)

    def __str__(self):
        return f"{User.username} Tasks"


class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    date_start = models.DateTimeField(default=timezone.now)
    duration = models.TimeField(default=timezone.now)
    date_posted = timezone.now()
    tasks = models.ForeignKey(to=Tasks, on_delete=models.CASCADE, default=None)  # maybe not on delete? since users can have common tasks
    
    def __str__(self):
        return f"{self.title}"
