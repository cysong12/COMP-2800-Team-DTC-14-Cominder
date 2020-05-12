from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from Apps.task_tracker.models import BuiltInTask


# Create your models here.

class SubForum(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)


class Post(models.Model):
    title = models.CharField(max_length=20)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = datetime.now()
    description = models.CharField(max_length=200)
    likes = models.IntegerField(default=0, null=True, blank=True)
    sub_forum = models.ForeignKey(SubForum, on_delete=models.CASCADE)


class Comment(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = datetime.now()
    message = models.CharField(max_length=500)
    on_post = models.ForeignKey(Post, on_delete=models.CASCADE)


def testing():
    for categories in BuiltInTask.CATEGORY_CHOICES:
        SubForum(categories[1]).save()
