from django import forms
from Apps.task_tracker.models import *
from Apps.forums.models import *
from django.utils import timezone


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'category', 'description', 'date_start']


class TaskCompleteForm(forms.ModelForm):
    #title = forms.CharField(max_length=50)
    #description = forms.CharField(max_length=1000)

    class Meta:
        model = Post
        fields = ['title', 'description', 'sub_forum']

'''
class Post(models.Model):
    title = models.CharField(max_length=20)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = datetime.now()
    description = models.CharField(max_length=200)
    likes = models.IntegerField(default=0, null=True, blank=True)
    # file = models.FileField(upload_to=settings.MEDIA_ROOT, null=True, verbose_name="")
    sub_forum = models.ForeignKey(SubForum, on_delete=models.CASCADE)
    '''
