from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Task(models.Model):
    task_title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    date_posted = timezone.now()
    date_start = models.DateTimeField(default=timezone.now)
    duration = models.DateTimeField(default=datetime.timedelta(hours=24))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task_title
