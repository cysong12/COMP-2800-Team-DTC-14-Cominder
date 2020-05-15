from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.forums, name='forums-main'),
    path('posts/', views.PostList.as_view(), name='user-preference-subforums-posts'),
    path('home/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('home/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('home/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('subforum/<int:pk>/', views.subforum_posts, name='subforum-home'),
    path('/$', views.increment_like, name='increment-like'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
