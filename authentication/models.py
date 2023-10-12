from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    pan = models.IntegerField(unique=True, null=True, blank=True)
    vat = models.IntegerField(unique=True, null=True, blank=True)
    phone_number = models.IntegerField(unique=True)
    
class User(AbstractUser):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, default = "default_username")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    
    # loging in from email
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']
