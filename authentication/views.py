from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from .serillizers import *
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password


# Create your views here.
class UserApiView(APIView):
    
    def get(self, request):
        user = User.objects.all()
        serilizers = GetUserSerilizers(user, many = True)       
        if user:
            return Response(serilizers.data)
        else:
            return Response("error")
        
    
    def post(self, request):
        serilizer = UserSerilizers(data=request.data)
        if serilizer.is_valid():
            hashed_password = make_password(request.data['password'])
            serilizer.validated_data['password'] = hashed_password
            serilizer.save()
            return Response("User Created")
        else:
            return Response("Validation error!!!")
        
class LoginApiView(APIView):
    
    def post(self, request):
        username = request.data.get('email')       
        password = request.data.get('password')
        auth = authenticate(username=username, password=password)
        # print(auth, username, password)
        if auth is not None:
            login(request, auth)
            return Response("Login SucessFull")
        else:
            return Response("Try Again")
        

class LogoutApiView(APIView):
    
    def get(self, request):       
        user = request
        logout(user)
        
        return Response("Logout Sucessfull")
            
class SupplierApIView(APIView):
    
    def get(self, request):
        supplier_obj = Supplier.objects.all()
        serializer = GetSupplierSerilizers(supplier_obj, many=True)        
        if supplier_obj:
            return Response(serializer.data)
        else:
            return Response("No Data Found")
    
    def post(self, request):
        serilizer = SupplierSerilizers(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors)

    