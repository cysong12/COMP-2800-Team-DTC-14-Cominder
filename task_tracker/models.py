from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):
    task_title = models.CharField(max_length=20)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
