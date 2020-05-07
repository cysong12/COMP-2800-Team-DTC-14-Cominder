from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.landing_page, name='feature-landing'),
	path('home/', views.home, name='task-tracker-home'),
	path('about/', views.about, name='task-tracker-about'),
	path('contact/', views.contact, name='feature-contact')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)