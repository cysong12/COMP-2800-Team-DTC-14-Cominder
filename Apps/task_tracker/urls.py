from django.urls import path
from . import views
from .views import TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing_page, name='feature-landing'),
    path('home/<uuid:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('home/<uuid:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('home/<uuid:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('home/<uuid:pk>/complete', views.complete, name='complete'),
    path('home/new/', TaskCreateView.as_view(), name='task-create'),
    path('home/', views.home, name='task-tracker-home'),
    path('about/', views.about, name='task-tracker-about'),
    path('contact/', views.contact, name='feature-contact'),
    path('home/<uuid:pk>/complete-no-upload', views.complete_no_upload, name='complete-no-upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
