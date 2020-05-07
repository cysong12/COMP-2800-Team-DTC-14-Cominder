from django import forms
from Apps.task_tracker.models import Task
from django.utils import timezone


class TaskForm(forms.ModelForm):
    name = forms.CharField()
    task_title = forms.CharField()
    description = forms.CharField()
    # date_start = forms.DateTimeField(default=timezone.now())
    duration = forms.TimeField()

    class Meta:
        model = Task
        # fields = ('name', 'task_title', 'description', 'date_start', 'duration')
        fields = ('name', 'task_title', 'description', 'duration')
