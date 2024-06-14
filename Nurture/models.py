from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images',null=True)
    status=models.BooleanField(default=False)

    def __str__(self) :
        return self.name


class Subcategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory_name=models.CharField(max_length=200)
    subcategory_image=models.ImageField(upload_to='images',null=True)
    def __str__(self) :
        return self.subcategory_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_image=models.ImageField(upload_to='images',null=True)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    original_price=models.IntegerField(null=False)
    selling_price=models.IntegerField(null=False)
    quantity=models.IntegerField(null=False,blank=False)
    description=models.TextField(max_length=700,null=False,blank=False)
    season=models.TextField(max_length=600,null=False,blank=False)
    scientific_name=models.CharField(max_length=100,null=False,blank=False)
    family=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.product_name
    
class Cart(models.Model):
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    qnty=models.IntegerField(null=False,default=1)
    date=models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    order_item=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    order_status=models.BooleanField(null=True)
    address=models.TextField(null=False)
    price=models.IntegerField(null=True)
    
    