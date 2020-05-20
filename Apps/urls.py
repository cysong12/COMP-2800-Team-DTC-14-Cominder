from . import views as main_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .users import views as user_views

urlpatterns = [
    path('', main_views.landing_page, name='feature-landing'),
    path('home/', main_views.home, name='feature-home'),
    path('about/', main_views.about, name='feature-about'),
    path('contact/', main_views.contact, name='feature-contact'),
    path('share/', main_views.social_share, name='feature-share'),
    path('task-tracker/', include('Apps.task_tracker.urls')),
    path('forums/', include('Apps.forums.urls')),
    path('heat-map/', include('Apps.heat_map.urls')),
    path('leaderboard/', user_views.leaderboard, name='feature-leaderboard'),
    path('fridge/', include('Apps.fridge.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
