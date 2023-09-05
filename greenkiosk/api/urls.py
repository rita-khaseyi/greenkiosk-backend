from django.urls import path
from .views import (
    CustomerListView,
    CustomerDetailView,
    ProductListView,
    ProductDetailView,
    OrderListView,
    OrderDetailView,
    CartListView,
    CartDetailView,
    add_to_cart
   
)

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer_list_view'),
    path('customers/<int:id>/', CustomerDetailView.as_view(), name='customer_detail_view'),
    
    path('products/', ProductListView.as_view(), name='Products_list_view'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='Products_detail_view'),
    
    path('orders/', OrderListView.as_view(), name='Orders_list_view'),
    path('orders/<int:id>/', OrderDetailView.as_view(), name='orders_detail_view'),
    
    # URLs for the Cart model
    path('carts/', CartListView.as_view(), name='cart_list_view'),
    path('carts/<int:pk>/', CartDetailView.as_view(), name='cart_detail_view'),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    
]
