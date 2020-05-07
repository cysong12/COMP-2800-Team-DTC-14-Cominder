from django.db import models
from django.contrib.auth.models import User
from Apps.task_tracker.models import Task
from django.utils import timezone


'''
class Tasks(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{User.username} Tasks'
'''


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
