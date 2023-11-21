from django.shortcuts import render
from . serillizers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class CustomerViewApi(APIView):
    serilizers = CustomerSerializers
    
    def get(self, request):
        customer_obj = Customer.objects.all()
        serilizers = self.serilizers(customer_obj,  many = True)
        
        if serilizers:
            return Response(serilizers.data)
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
            return Response('No data found')
        return Response('error!!!!')
        