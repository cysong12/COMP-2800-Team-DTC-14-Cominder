from django import forms
from Apps.task_tracker.models import *
from django.utils import timezone


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'category', 'description', 'date_start']
