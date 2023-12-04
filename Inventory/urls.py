from django.urls import path
from .views import *

urlpatterns = [
    path('customer/', CustomerViewApi.as_view(), name='customer'),
    path('customer/<int:pk>', CustomerViewApi.as_view(), name='customer')
]