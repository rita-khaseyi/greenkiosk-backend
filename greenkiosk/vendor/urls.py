from django.urls import path
from .views import upload_vendor
from .views import vendor_list
from .views import vendor_detail
from .views import vendor_edit_view


urlpatterns = [
    path('vendor/upload', upload_vendor, name='vendor_upload_view'),
    path('vendor/list', vendor_list, name='vendor_list_view'),
    path('vendor/<int:id>/', vendor_detail, name='vendor_detail_view'),
    path('vendor/edit/<int:id>/', vendor_edit_view, name='vendor_edit_view'),
    
    
]


