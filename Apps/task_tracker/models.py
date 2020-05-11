from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


class CustomTask(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    date_start = models.DateTimeField(default=datetime.now)
    date_posted = models.DateTimeField(default=datetime.now)
    duration = models.TimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})


class BuiltInTask(models.Model):
    title = models.CharField(max_length=20)
    SPORTS = 'sports'
    GAMES = 'games'
    COOKING = 'cooking'
    OTHER = 'other'
    CATEGORY_CHOICES = [
        (SPORTS, 'Sports'),
        (GAMES, 'Games'),
        (COOKING, 'Cook'),
        (OTHER, 'Other')
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=OTHER)
    description = models.TextField(null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    '''
    date_start = models.DateTimeField(default=datetime.now)
    date_created = models.DateTimeField(default=datetime.now)
    duration = models.TimeField(default=timezone.now)
    '''

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})
