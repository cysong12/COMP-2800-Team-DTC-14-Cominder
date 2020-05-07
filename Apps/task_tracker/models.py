from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
<<<<<<< HEAD
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
=======
    date_start = models.DateTimeField(default=timezone.now)
    duration = models.TimeField(default=timezone.now)
    date_posted = timezone.now()
    # tasks = models.ForeignKey('users.Tasks', on_delete=models.CASCADE)  # maybe not on delete? since users can have common tasks
>>>>>>> choi_branch2
    
    def __str__(self):
        return self.title
