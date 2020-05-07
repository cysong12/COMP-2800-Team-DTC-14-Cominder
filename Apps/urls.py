from . import views as main_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', main_views.landing_page, name='feature-landing'),
    path('home/', main_views.home, name='feature-home'),
    path('about/', main_views.about, name='feature-about'),
    path('contact/', main_views.contact, name='feature-contact'),
    path('task-tracker/', include('Apps.task_tracker.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
