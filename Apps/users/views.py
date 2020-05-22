from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from Apps.task_tracker.models import *
from Apps.forums.models import *
from .models import *
from django.views.generic import ListView


def settings(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.Post, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your account has been updated.")
            return redirect('feature-home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/settings.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_created = form.save()
            all_categories = Category.objects.all()
            profile_instance = Profile.objects.get(user=user_created)
            profile_instance.preferences.set(all_categories)
            profile_instance.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created! Log in and change some habits!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'base/base.html')


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/update_profile.html', context)


class ProfileListView(ListView):
    model = Profile
    template_name = 'users/leaderboard.html'
    context_object_name = 'profiles'
    ordering = ['points']
    paginate_by = 5
    
    def get_queryset(self):
        return Profile.objects.all().exclude(user__is_superuser=True)
