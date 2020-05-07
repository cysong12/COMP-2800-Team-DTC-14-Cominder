from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    # date_posted = timezone.now()
    # date_start = models.DateTimeField(default=timezone.now, null=True, blank=True)
    # duration = models.DateTimeField(default=datetime.timedelta(hours=24), null=True, blank=True)
    # tasks = models.ForeignKey('users.Tasks', on_delete=models.CASCADE)  # maybe not on delete? since users can have common tasks
    
    def __str__(self):
        return self.title
