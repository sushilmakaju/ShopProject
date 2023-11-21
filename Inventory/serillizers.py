from .models import *
from rest_framework import serializers


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class OrderSerialiers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class OrderDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'
        
class BillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'