from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CustomTask
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


@login_required
def home(request):
    tasks = CustomTask.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'task_tracker/home.html', context)


class CustomTaskListView(ListView):
    model = CustomTask
    template_name = 'task_tracker/home.html'
    context_object_name = 'tasks'
    ordering = ['date_posted']

    def get_queryset(self):
        queryset = super(CustomTaskListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class CustomTaskDetailView(DetailView):
    model = CustomTask


class CustomTaskCreateView(LoginRequiredMixin, CreateView):
    model = CustomTask
    success_url = '/task-tracker/home'
    fields = ['title', 'description', 'date_start']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CustomTaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomTask
    success_url = '/task-tracker/home'
    fields = ['title', 'description', 'date_start']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


class CustomTaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CustomTask
    success_url = '/task-tracker/home'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


def about(request):
    return render(request, 'task_tracker/about.html', {'title': 'About us'})


def landing_page(request):
    return render(request, 'main/landing_page.html')


def contact(request):
    return render(request, 'main/contact.html')
