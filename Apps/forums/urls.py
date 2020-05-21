from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.forums, name='forums-main'),
    path('posts/', views.PostList.as_view(), name='user-preference-subforums-posts'),
    path('home/<int:pk>/', views.post_detail_view, name='post-detail'),
    path('home/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('home/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('subforum/<int:pk>/', views.SubforumPostsList.as_view(), name='subforum-home'),
    url(r'^like/$', views.like, name='like'),
    url(r'^comment_like/$', views.comment_like, name='comment-like'),
    # path('home/<int:pk>/', views.post_detail_view, name='comment-form')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
