from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import *
from django.http import HttpResponseRedirect


@login_required
def home(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    context = {
        'tasks': tasks,
        'categories': categories,
    }
    return render(request, 'task_tracker/home.html', context)

'''class Post(models.Model):
    title = models.CharField(max_length=20)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = datetime.now()
    description = models.CharField(max_length=200)
    likes = models.IntegerField(default=0, null=True, blank=True)
    # file = models.FileField(upload_to=settings.MEDIA_ROOT, null=True, verbose_name="")
    sub_forum = models.ForeignKey(SubForum, on_delete=models.CASCADE)'''


def task_complete_form_to_creating_post(request, form_response):
    post_created = Post.objects.create(title=form_response['title'], posted_by=request.user,
                                       description=form_response['description'], sub_forum=form_response['sub_forum'])
    return post_created


def complete(request, pk):
    task_instance = get_object_or_404(Task, pk=pk)
    post_created = ''
    if request.method == "POST":
        form = TaskCompleteForm(request.POST)
        if form.is_valid():
            task_instance.completed = True
            form_response = form.cleaned_data
            post_created = task_complete_form_to_creating_post(request, form_response)
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
