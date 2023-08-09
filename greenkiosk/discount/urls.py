from django.urls import path
from .views import upload_discount
from .views import discount_list
from .views import discount_detail
from .views import edit_discount_view


urlpatterns = [
    path('discount/upload', upload_discount, name='discount_upload_view'),
    path('discount/list', discount_list, name='discount_list_view'),
    path('discount/<int:id>/', discount_detail, name='discount_detail_view'),
    path('discount/edit/<int:id>/', edit_discount_view, name='discount_edit_view'),
    
    
]


