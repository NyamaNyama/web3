from django.urls import path
from .views import *

urlpatterns = [
    path('add_image/', add_image, name='add_image'),
    
    path('delete_image/', delete_image, name='delete_image'),
    
    path('',index,name='index')
]