from django import forms
from Apps.task_tracker.models import Task
from django.utils import timezone


class TaskForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField()
    # date_start = forms.DateTimeField()
    # duration = forms.TimeField()

    class Meta:
        model = Task
        fields = ('title', 'description') #'date_posted')#, 'date_start', 'duration')
        # fields = ('name', 'task_title', 'description', 'duration')
