from django.urls import path
from . import views

urlpatterns = [
	path('', views.landing_page, name='task-tracker-home'),
	path('about/', views.about, name='task-tracker-about'),
]