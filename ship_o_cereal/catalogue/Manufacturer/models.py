from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    ManID = models.IntegerField(primary_key=True, serialize=True)
    Name = models.CharField(max_length=255)


class ManufacturerLogo(models.Model):
    ManID = models.OneToOneField(Manufacturer, on_delete=models.CASCADE, unique=True)
    Image = models.CharField(max_length=9999)