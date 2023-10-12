from django.urls import path
from .views import *

urlpatterns = [
    path('user', UserApiView.as_view()),
    path('login', LoginApiView.as_view(), name="login"),
    path('logout', LogoutApiView.as_view(), name="logout"),
    path('supplier', SupplierApIView.as_view(), name="supplier")
]
