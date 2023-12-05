from django.urls import path
from .views import *

urlpatterns = [
    path('customer/', CustomerViewApi.as_view(), name='customer'),
    path('customer/<int:pk>', CustomerViewApi.as_view(), name='customer'),
    
    path('product/', ProductApiView.as_view(), name='product'),
    path('product/<int:pk>', ProductApiView.as_view(), name='product'),
    
]