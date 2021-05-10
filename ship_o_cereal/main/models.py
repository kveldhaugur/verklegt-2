from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


class Manufacturer(models.Model):
    ManID = models.IntegerField(primary_key=True, serialize=True)
    Name = models.CharField(max_length=255)
    def __str__(self):
        return self.Name


class ManufacturerLogo(models.Model):
    ManID = models.OneToOneField(Manufacturer, on_delete=models.CASCADE, unique=True)
    Image = models.CharField(max_length=9999)


class ItemCategory(models.Model):
    CategoryID = models.IntegerField(primary_key=True, serialize=True)
    CategoryTag = models.CharField(max_length=255)
    def __str__(self):
        return self.CategoryTag


class Items(models.Model):
    ItemID = models.IntegerField(primary_key=True, serialize=True)
    ManID = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    Quantity_available = models.IntegerField()
    Price = models.IntegerField()
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=9999, blank=True)
    Image = models.CharField(max_length=255, null=True)
    Tags = models.ManyToManyField(ItemCategory)
    def __str__(self):
        return self.Name


class Country(models.Model):
    CountryName = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.CountryName}'

class UserInfo(models.Model):
    AccountConnected = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    PostalCode = models.CharField(max_length=15)
    Address = models.CharField(max_length=255)
    HouseNum = models.IntegerField()
    MobilePhone = models.CharField(max_length=63)
    Email = models.CharField(max_length=255)
    SSN = models.CharField(max_length=255)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)


class OrderContains(models.Model):
    ItemID = models.ForeignKey(Items, on_delete=models.CASCADE)
    Quantity = models.IntegerField(null=False)


class Order(models.Model): #has id
    AccountID = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    ItemsInOrder = models.ManyToManyField(OrderContains)


class UserImage(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Image = models.URLField(max_length=9999, null=True)


class SessionHistory(models.Model):
    SessionID = models.ForeignKey(Session, on_delete=models.CASCADE, null=False)
    HistoryStr = models.CharField(max_length=255)

# Create your models here.
