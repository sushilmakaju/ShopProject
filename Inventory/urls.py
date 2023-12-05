from django.urls import path
from .views import *

urlpatterns = [
    path('customer/', CustomerViewApi.as_view(), name='customer'),
    path('customer/<int:pk>', CustomerViewApi.as_view(), name='customer'),
    
    path('product', ProductApiView.as_view(), name='product'),
    path('product/<int:pk>', ProductApiView.as_view(), name='product'),
    
    path('order', OrderApiView.as_view(), name='order'),
    path('order/<int:pk>', OrderApiView.as_view(), name='order'),
    
    path('order-details', OrderdetailsApiView.as_view(), name='order-details'),
    path('order-details/<int:pk>', OrderdetailsApiView.as_view(), name='order-details'),
    
    path('bill/', GenerateBillAPIView.as_view(), name='bill'),
    
]