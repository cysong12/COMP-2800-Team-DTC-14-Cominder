from django.urls import path
from .views import FridgeCreateView, FridgeDetailView, FridgeUpdateView, FridgeDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='fridge-home'),
    path('new/', FridgeCreateView.as_view(), name='fridge-create'),
    path('item/<uuid:pk>', FridgeDetailView.as_view(), name='fridge-detail'),
    path('item/<uuid:pk>/update/', FridgeUpdateView.as_view(), name='fridge-update'),
    path('item/<uuid:pk>/delete/', FridgeDeleteView.as_view(), name='fridge-delete'),
]