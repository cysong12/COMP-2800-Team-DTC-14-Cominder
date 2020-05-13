from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from Apps.task_tracker.models import *
from Cominder import settings


# Create your models here.

class SubForum(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(max_length=20)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = datetime.now()
    description = models.CharField(max_length=200)
    likes = models.IntegerField(default=0, null=True, blank=True)
    media = models.FileField(default='post_media/default.jpg', upload_to='post_media')
    sub_forum = models.ForeignKey(SubForum, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    message = models.CharField(max_length=500)
    on_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.posted_by}"


'''
class CommentLike(models.Model):
    pass


class PostLike(models.Model):
    pass
'''
