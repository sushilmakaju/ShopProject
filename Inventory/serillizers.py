from .models import *
from rest_framework import serializers

class CustomerSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'