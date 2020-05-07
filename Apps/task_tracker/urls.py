from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
	path('', views.landing_page, name='feature-landing'),
	path('home/', PostListView.as_view(), name='feature-home'),
	path('about/', views.about, name='feature-about'),
	path('contact/', views.contact, name='feature-contact')
]
