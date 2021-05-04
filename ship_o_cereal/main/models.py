from django.db import models


from catalogue.Items.models import Items


class ItemCategory(models.Model):
    CategoryID = models.IntegerField(primary_key=True, serialize=True)
    CategoryTag = models.CharField(max_length=255)


class Country(models.Model):
    CountryID = models.IntegerField(primary_key=True, serialize=True)
    CountryName = models.CharField(max_length=255)


class Account(models.Model):
    AccountID = models.IntegerField(primary_key=True, serialize=True)
    AccountName = models.CharField(max_length=255)
    AccountPass = models.CharField(max_length=255)
    ProfilePic = models.CharField(max_length=255)
    DateOfBirth = models.DateTimeField(auto_now=False, null=True)


class UserInfo(models.Model):
    AccountConnected = models.OneToOneField('Account', primary_key=True, on_delete=models.CASCADE)
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


class Order(models.Model):
    OrderID = models.IntegerField(primary_key=True, serialize=True)
    AccountID = models.ForeignKey('Account', on_delete=models.CASCADE, null=False)
    ItemsInOrder = models.ManyToManyField('catalogue.Items')


class OrderContains(models.Model):
    ItemID = models.ForeignKey('catalogue.Items', on_delete=models.CASCADE)
    Quantity = models.IntegerField(null=False)

# Create your models here.
