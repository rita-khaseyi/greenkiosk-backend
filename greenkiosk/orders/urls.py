# orders/urls.py
from django.urls import path
from .views import create_order, order_confirmation

urlpatterns = [
    path('checkout/', create_order, name='checkout'),
    path('order_confirmation/', order_confirmation, name='order_confirmation'),
]
