from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='task-tracker-home'),
	path('about/', views.about, name='blog-about'),
]