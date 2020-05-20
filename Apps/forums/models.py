from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from Apps.task_tracker.models import *
from Cominder import settings
from django.template.defaultfilters import slugify


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
    likes = models.ManyToManyField(User, related_name='post_likes')
    # comments = models.ForeignKey(Comment, related_name='comments')
    slug = models.SlugField()
    media = models.FileField(default='post_media/default.jpg', upload_to='post_media')
    sub_forum = models.ForeignKey(SubForum, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commented_user')
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='comment_likes')
    message = models.CharField(max_length=500)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    on_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.posted_by}"

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['posted_date']


'''
class CommentLike(models.Model):
    pass


class PostLike(models.Model):
    pass
'''
