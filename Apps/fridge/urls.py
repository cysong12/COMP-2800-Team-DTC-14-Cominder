from django.urls import path
from .views import FridgeListView, FridgeCreateView, FridgeDetailView, FridgeUpdateView, FridgeDeleteView
from . import views

urlpatterns = [
    path('', FridgeListView.as_view(), name='fridge-home'),
    path('new/', FridgeCreateView.as_view(), name='fridge-create'),
    path('item/<int:pk>', FridgeDetailView.as_view(), name='fridge-detail'),
    path('item/<int:pk>/update/', FridgeUpdateView.as_view(), name='fridge-update'),
    path('item/<int:pk>/delete/', FridgeDeleteView.as_view(), name='fridge-delete'),
]