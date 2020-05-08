from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    duration = models.TimeField(default=timezone.now)
    username = User.username
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})
