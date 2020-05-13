from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from Apps.task_tracker.models import *
from Apps.forums.models import *


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    points = models.IntegerField(default=0, null=True, blank=True)
    preferences = models.ManyToManyField(to=Category)
    
    def __str__(self):
        return f'{self.user.username} Profile'
