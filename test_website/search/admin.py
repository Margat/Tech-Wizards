from django.contrib import admin
from . models import Car, Customer, Store, Order
# Register your models here.
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Store)
admin.site.register(Order)
