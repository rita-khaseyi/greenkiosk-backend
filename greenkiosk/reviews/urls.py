from django.urls import path
from .views import upload_review
from .views import review_list
from .views import review_detail
from .views import review_edit_view


urlpatterns = [
    path('review/upload', upload_review, name='review_upload_view'),
    path('review/list', review_list, name='review_list_view'),
    path('review/<int:id>/', review_detail, name='review_detail_view'),
    path('review/edit/<int:id>/', review_edit_view, name='review_edit_view'),
    
    
]


