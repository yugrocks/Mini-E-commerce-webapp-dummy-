from django.db import models

class User(models.Model): 
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    contact=models.IntegerField()
    address=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class Product(models.Model):
    product_name=models.CharField(max_length=200)
    cost=models.IntegerField()
    imagename=models.CharField(max_length=200)
    category=models.CharField(max_length=100)
    
class Wishlist(models.Model): 
    email=models.CharField(max_length=200)
    product_name=models.CharField(max_length=200)

class Kart(models.Model):
    email=models.CharField(max_length=200)
    product_name=models.CharField(max_length=200)
