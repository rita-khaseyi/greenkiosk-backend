from django.urls import path
from .views import upload_product
from .views import product_list
from .views import product_detail

urlpatterns = [
    path('products/upload', upload_product, name='product_upload_view'),
    path('products/list', product_list, name='products_list_view'),
    path('products/<int:id>/', product_detail, name='products_detail_view'),
]


