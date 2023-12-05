from django.shortcuts import render
from . serillizers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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
            product_obj = Product.objects.all()
            product_serializers = ProductSerializers(product_obj, many=True) 
            if product_serializers:
                return Response(product_serializers.data)
            return Response('no data found')
        else:
            product_obj = Product.objects.get(id=pk)
            product_serializers = ProductSerializers(product_obj)
            if product_serializers:
                return Response(product_serializers.data)
            return Response('no data found')
        
    def post(self, request):
        product_serializer = ProductSerializers(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response('Data Created')
        return Response(product_serializer.errors)
    
    def put(self, request, pk):
        try:
            product_obj = Product.objects.get(id=pk)
        except:
            return Response('No data found')
        product_serializers = ProductSerializers(product_obj, data=request.data)
        if product_serializers.is_valid():
            product_serializers.save()
            return Response('data updated')
        return Response(product_serializers.errors)
    
    def delete(self, request, pk):
        try:
            product_obj = Product.objects.get(id=pk)
        except:
            return Response('No data found')

        product_obj.delete()
        return Response('Data deleted') 
    
class OrderApiView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            try:
                order_obj = Order.objects.get(id=pk)
            except:
                return Response('no data found')
            order_serilizer = OrderSerialiers(order_obj)
            if order_serilizer:
                return Response(order_serilizer.data)
        else:
            order_obj = Order.objects.all()
            order_serilize = OrderSerialiers(order_obj, many=True)
            if order_serilize:
                return Response(order_serilize.data)
            return Response('No data found')
        
    def post(self,request):
        order_serializer = OrderSerialiers(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response('data created')
        return Response(order_serializer.errors)
    
    def put(self, request, pk):
        order_obj = Order.objects.get(id=pk)
        if order_obj:
            order_serilizers = OrderSerialiers(order_obj, data=request.data)
            if order_serilizers.is_valid():
                order_serilizers.save()
                return Response('data updated')
            return Response(order_serilizers.errors)
        else:
            return Response('NO data found')
        
    def delete(self, request, pk):
        order_obj = Order.objects.get(id=pk)
        if order_obj:
            order_obj.delete()
            return Response('Data Deleted')
        return Response('No data found')
    

class OrderdetailsApiView(APIView):
    def get(self,request, pk=None):
        if pk:
            orderdetail_obj = OrderDetails.objects.get(id=pk)
            if orderdetail_obj:
                orderdetail_serilizer = OrderDetailsSerializers(orderdetail_obj)
                return Response(orderdetail_serilizer.data)
            return Response('No data found')
        else:
            orderdetaik_obj = OrderDetails.objects.all()
            orderdetail_serilizers = OrderDetailsSerializers(orderdetaik_obj, many=True)
            if orderdetail_serilizers:
                return Response(orderdetail_serilizer.data)
            return Response('No data found')
        
    def post(self, request):
        
        orderdetails_serializer = OrderDetailsSerializers(data=request.data)
        if orderdetails_serializer.is_valid():
            orderdetails_serializer.save()
            return Response('Data Created')
        return Response(orderdetails_serializer.errors)
    
    def delete(self, request, pk):
        order_details_object = OrderDetails.objects.get(id=pk)
        if order_details_object:
            order_details_object.delete()
            return Response('data deleted')
        return Response('No data found')
    
    def put(self, request, pk):
        orderdetails_obj = OrderDetails.objects.get(id=pk)
        if orderdetails_obj:
            orderdetails_serailizer = OrderDetailsSerializers(orderdetails_obj, data=request.data)
            if orderdetails_serailizer.is_valid():
                return Response('Data Updated')
            return Response(orderdetails_serailizer.errors)
        
    
class GenerateBillAPIView(APIView):
    def post(self, request, order_details_id):

        order_details = get_object_or_404(OrderDetails, pk=order_details_id)
        total_amount = self.calculate_total_amount(order_details)
        bill = Bill(
            bill_no=self.get_unique_bill_number(), 
            order_details=order_details, 
            total_amount=total_amount
            )
        bill.save()
        serializer = BillSerializers(bill)
        return Response(serializer.data)

    def calculate_total_amount(self, order_details):

        total_amount = 0
        for item in order_details.product.all():
            total_amount += item.quantity * item.unit_price
        return total_amount

    def get_unique_bill_number(self):
        return f'BILL-{Bill.objects.count() + 1}'
    
    

        
                 
            
            
        
            
                            