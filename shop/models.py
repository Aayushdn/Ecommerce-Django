from django.db import models
from django.db.models.base import Model

# Create your models here.
class Product(models.Model):

    Product_id = models.AutoField(primary_key=True)
    Product_name = models.CharField(max_length=200)
    Product_descr = models.CharField(max_length=600)
    category = models.CharField(max_length = 50 , default='')
    Sub_category = models.CharField(max_length = 50 ,default='')
    image = models.ImageField(upload_to = "shop/images",default='')
    price = models.IntegerField(default=0)
    Poduct_Pub_date = models.DateField()

    def __str__(self):
        return self.Product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    desc = models.CharField(max_length=1200)


    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    itemJSon = models.CharField(max_length=50000 , default='')
    itemsName = models.CharField(default = '', max_length=500000)
    amount = models.IntegerField(default = 0)
    name = models.CharField(max_length=200,default='')
    email = models.CharField(max_length=200,default='')
    address = models.CharField(max_length=200,default='')
    phone = models.CharField(max_length=200,default='')
    city = models.CharField(max_length=200,default='')
    zip_code = models.CharField(max_length=200,default='')
    state = models.CharField(max_length=200,default='')
    
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    update_desc = models.CharField(default="", max_length = 5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[:10]


    
