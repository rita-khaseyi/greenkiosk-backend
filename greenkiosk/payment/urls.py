from django.urls import path
from .views import upload_product,payment_list,payment_detail,edit_payment_view



urlpatterns = [
    path('payment/upload', upload_product, name='paymentupload_view'),
    path('payment/list', payment_list, name='payment_list_view'),
    path('payment/<int:id>/', payment_detail, name='payment_detail_view'),
    path('payment/edit/<int:id>/', edit_payment_view, name='edit_payment_view'),
    
 
    
    
]
