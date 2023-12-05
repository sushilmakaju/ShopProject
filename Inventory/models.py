from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.EmailField()
    PAN = models.IntegerField(null=True, blank=True, unique=True)
    VAT = models.IntegerField(null=True, blank=True, unique=True)
    
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    unit = models.IntegerField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
class Order(models.Model):
    order_date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
 
class OrderDetails(models.Model):
    unit_price = models.IntegerField()
    quantity = models.IntegerField
    discount = models.DecimalField(max_digits=5,  decimal_places=2)
    total = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    


class Bill(models.Model):
    bill_no = models.IntegerField()
    order_details = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)