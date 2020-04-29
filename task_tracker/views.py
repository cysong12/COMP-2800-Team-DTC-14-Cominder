from django.shortcuts import render


def home(request):
	return render(request, 'task_tracker/home.html')


def about(request):
	return render(request, 'task_tracker/about.html')


def landing_page(request):
	return render(request, 'task_tracker/landing_page.html')
