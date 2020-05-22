from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
import uuid


class Category(models.Model):
    SPORTS = 'Sports'
    GAMES = 'Games'
    COOKING = 'Cook'
    CUSTOM = 'Custom'
    CATEGORY_CHOICES = [
        (SPORTS, 'Sports'),
        (GAMES, 'Games'),
        (COOKING, 'Cook'),
        (CUSTOM, 'Custom')
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, unique=True, default=CUSTOM)

    def __str__(self):
        return f"{self.category}"


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    date_start = models.DateTimeField(default=datetime.now)
    date_posted = models.DateTimeField(default=datetime.now)
    duration = models.TimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})
