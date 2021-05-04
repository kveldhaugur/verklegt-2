from django.db import models

# Create your models here.


from catalogue.Manufacturer.models import Manufacturer


class Items(models.Model):
    ItemID = models.IntegerField(primary_key=True, serialize=True)
    ManID = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    Quantity_available = models.IntegerField()
    Price = models.IntegerField()
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=9999, blank=True)
    Tags = models.ManyToManyField('ItemCategory')