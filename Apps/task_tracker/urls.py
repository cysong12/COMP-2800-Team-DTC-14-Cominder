from django.urls import path
from . import views
from .views import CustomTaskListView, CustomTaskDetailView, CustomTaskCreateView, CustomTaskUpdateView, CustomTaskDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing_page, name='feature-landing'),
    path('home/<int:pk>/', CustomTaskDetailView.as_view(), name='task-detail'),
    path('home/<int:pk>/update', CustomTaskUpdateView.as_view(), name='task-update'),
    path('home/<int:pk>/delete', CustomTaskDeleteView.as_view(), name='task-delete'),
    path('home/new/', CustomTaskCreateView.as_view(), name='task-create'),
    path('home/', CustomTaskListView.as_view(), name='task-tracker-home'),
    path('about/', views.about, name='task-tracker-about'),
    path('contact/', views.contact, name='feature-contact')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
