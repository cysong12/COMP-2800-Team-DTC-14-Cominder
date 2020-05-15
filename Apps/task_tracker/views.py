from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q


@login_required
def home(request):
    tasks = Task.objects.filter(Q(completed=False))
    categories = Category.objects.all()
    context = {
        'tasks': tasks,
        'categories': categories,
    }
    return render(request, 'task_tracker/home.html', context)


def complete_no_upload(request, pk):
    task_instance = get_object_or_404(Task, pk=pk)
    task_instance.completed = True
    task_instance.save(update_fields=["completed"])
    return redirect('task-tracker-home')


def task_complete_form_to_creating_post(request, form_response):
    post_created = Post.objects.create(title=form_response['title'], posted_by=request.user,
                                       description=form_response['description'], sub_forum=form_response['sub_forum'],
                                       media=form_response['media'])
    post_created.save()
    return post_created


def complete(request, pk):
    task_instance = get_object_or_404(Task, pk=pk)
    post_created = ''
    if request.method == "POST":
        form = TaskCompleteForm(request.POST, request.FILES)
        if form.is_valid():
            form_response = form.cleaned_data
            post_created = task_complete_form_to_creating_post(request, form_response)
            task_instance.completed = True
            task_instance.save(update_fields=["completed"])
            
            return redirect('post-detail', pk=post_created.pk)
    else:
        form = TaskCompleteForm()

    context = {
        'form': form,
        'task': task_instance,
    }

    return render(request, 'task_tracker/task_complete.html', context)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    success_url = '/task-tracker/home'
    fields = ['title', 'category', 'description', 'date_start']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.fields['category'] = Category.category
        return super().form_valid(form)


class TaskDetailView(DetailView):
    model = Task


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
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
