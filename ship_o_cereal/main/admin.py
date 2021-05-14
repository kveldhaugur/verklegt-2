from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Items)
admin.site.register(Manufacturer)
admin.site.register(ItemCategory)
admin.site.register(Country)
admin.site.register(UserInfo)
admin.site.register(ShippingInfo)
admin.site.register(PromoCodes)
admin.site.register(CartContains)
admin.site.register(OrderContains)
admin.site.register(Order)
admin.site.register(UserImage)
admin.site.register(SessionHistory)

