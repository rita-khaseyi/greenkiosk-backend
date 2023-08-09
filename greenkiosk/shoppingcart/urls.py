from django.urls import path
from .views import upload_Cart,shopping_list,shopping_detail,edit_shopping_view



urlpatterns = [
    path('cart/upload', upload_Cart, name='shoppingcart_upload_view'),
    path('cart/list', shopping_list, name='cart_list_view'),
    path('cart/<int:id>/', shopping_detail, name='cart_detail_view'),
    path('cart/edit/<int:id>/', edit_shopping_view, name='edit_cart_view'),
    
 
    
    
]


