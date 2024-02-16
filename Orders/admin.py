from django.contrib import admin
from Orders.models import Order, OrderDetail

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderDetail)