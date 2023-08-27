from django.urls import path
from .views import make_payment,user_payments,payment_confirmation


app_name = 'payment'
urlpatterns = [
    path('make-payment/', make_payment, name='make_payment'),
    path('user-payments/', user_payments, name='user_payments'),
    path('payment-confirmation/<int:payment_id>/', payment_confirmation, name='payment_confirmation'),
 
    
    
]
