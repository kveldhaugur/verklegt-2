from django.db import models


class ManufacturerLogo(models.Model):
    Image = models.CharField(max_length=9999)


class Manufacturer(models.Model):
    Name = models.CharField(max_length=255)
    Logo = models.ForeignKey(ManufacturerLogo, on_delete=models.CASCADE)


class Category(models.Model):
    CategoryTag = models.CharField(max_length=255)

class Product(models.Model):
    ManID = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    Quantity_available = models.IntegerField()
    Price = models.IntegerField()
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=9999)

class Tags(models.Model):
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    CategoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
#class Product(models.Model):

#class Order(models.Model):

#class OrderContains(models.Model):

#class Country(models.Model):

#class ShopingCart(models.Model):

#class CartContains(models.Model):


# Create your models here.
