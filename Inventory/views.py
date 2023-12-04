from django.shortcuts import render
from . serillizers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class CustomerViewApi(APIView):
    serilizers = CustomerSerializers
    
    def get(self, request, pk=None):
        if not pk:
            customer_obj = Customer.objects.all()
            serilizers = self.serilizers(customer_obj,  many = True)
            
            if serilizers:
                return Response(serilizers.data)
            else:
                return Response('Data Not Found')
        else:
            customer_obj = Customer.objects.get(id=pk)
            cus_serializers = CustomerSerializers(customer_obj)
            if cus_serializers:
                return Response(cus_serializers.data)
            else:
                return Response('Data Not Found')
                
        
    def post(self, request):
        
        seriliazer = self.serilizers(data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response('Data Created')
        return Response('validation errors', seriliazer.errors)
        
    def put(self, request, pk):
        try:
            customer_obj = Customer.objects.get(id = pk)
        except:
            return Response('Data Not Found!')
        serializer = self.serilizers(customer_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        try:
            customer_obj = Customer.objects.get(id = pk)
        except:
            return Response('Data Not Found')
        if customer_obj:
            customer_obj.delete()
            return Response('Data deleted')
        return Response('error!!!!')
    
class CategoryApiView(APIView):
    serializer_class = CategorySerializers
    
    def get(self, request, pk=None):
        if not pk:
            category_obj = Category.objects.all()
            category_serializers = self.serializer_class(category_obj, many=True)
            if category_serializers:
                return Response(category_serializers.data)
            return Response('No data found')
        else:
            category_obj = Category.objects.get(id=pk)
            category_serializer = self.serializer_class(category_obj)
            if category_serializer:
                return Response(category_serializer.data)
            return Response('No data found')
        
    def post(self, request):
        
        category_serializers = self.serializer_class(data=request.data)
        if category_serializers.is_valid():
            category_serializers.save()
            return Response('Data created', category_serializers.data)
        return Response(category_serializers.errors) 
            
    def put(self, request, pk):
        category_obj = Category.objects.get(id=pk)
        if category_obj:
            category_serialiers = self.serializer_class(category_obj, data=request.data)
            if category_serialiers.is_valid():
                category_serialiers.save()
                return Response('Data updated', category_serialiers.data)
            return Response('validation error', category_serialiers.errors)
        else:
            return Response('No data found')
            
    def delete(self, request, pk):
        category_obj = Category.objects.get(id=pk)
        if category_obj:
            category_obj.delete()
            return Response('Data deleted')
        return Response('No data found')
            
        
class ProductApiView(APIView):
    
    def get(self, request, pk=None):
        if not pk:
            pass              