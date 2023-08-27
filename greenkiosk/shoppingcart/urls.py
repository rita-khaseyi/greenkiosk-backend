from django.urls import path
from .views import view_cart,add_to_cart,remove_from_cart,update_cart_quantity



urlpatterns = [

    path('view-cart/',view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
     path('view_cart/<int:selected_product_id>/', view_cart, name='view_cart_with_selected'),
     path('update-cart-quantity/<int:cart_item_id>/', update_cart_quantity, name='update_cart_quantity'),
    
 
    
    
]


