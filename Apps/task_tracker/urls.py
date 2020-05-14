from django.urls import path, include
from . import views
from .views import TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing_page, name='feature-landing'),
    path('home/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('home/<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('home/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('home/<int:pk>/complete', views.complete, name='complete'),
    path('home/new/', TaskCreateView.as_view(), name='task-create'),
    path('home/', views.home, name='task-tracker-home'),
    path('about/', views.about, name='task-tracker-about'),
    path('contact/', views.contact, name='feature-contact'),
    path('send_push', send_push),	#WIP
	path('webpush/', include('views.webpush.urls')),		#WIP
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
