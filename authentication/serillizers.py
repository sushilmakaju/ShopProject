from .models import *
from rest_framework import serializers



class GetSupplierSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class SupplierSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class UserSerilizers(serializers.ModelSerializer):   
    class Meta:
        model = User
        fields = '__all__'

class GetUserSerilizers(serializers.ModelSerializer):     
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password']
        