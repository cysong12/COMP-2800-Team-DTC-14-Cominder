from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.landing_page, name='feature-landing'),
	path('home/', views.home, name='feature-home'),
	path('about/', views.about, name='feature-about'),
	path('contact/', views.contact, name='feature-contact'),
	path('send_push', send_push),	#WIP
	path('webpush/', include('views.webpush.urls'))		#WIP
]
