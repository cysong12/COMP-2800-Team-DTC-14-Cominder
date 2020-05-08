from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



@login_required
def home(request):
    context = {
        'tasks': Task.objects.filter(username=request.user.username)
    }
    return render(request, 'task_tracker/home.html', context)

class TaskListView(ListView):
    model = Task
    template_name = 'task_tracker/home.html'
    context_object_name = 'tasks'
    ordering = ['-date_posted']

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    success_url = '/task-tracker/home'
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
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
