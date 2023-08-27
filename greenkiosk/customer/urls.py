
from django.urls import path
from .views import login_view,logout_view,signup
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('customer/upload', upload_customer, name='customer_upload_view'),
    # path('customer/list', customer_list, name='customer_list_view'),
    # path('customer/<int:id>/', customer_detail, name='customer_detail_view'),
    # path('customer/edit/<int:id>/', edit_customer_view, name='customer_edit_view'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', signup, name='signup'),
 
    
    
]
