import csv
from django.contrib import admin
from django.http import HttpResponse
from . models import Car, Customer, Store, Order
# Register your models here.

def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='test/csv')
    response['Content-Disposition'] = 'attachment; filename="rentaldata.csv"'
    fields = [field.name for field in modeladmin.model._meta.fields]
    writer = csv.writer(response)
    writer.writerow(fields)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in fields])
    return response
    #https://djangosnippets.org/snippets/1697/

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'car_make', 'car_model', 'car_series', 'car_series_year', 'car_price_new', 'car_engine_size', 'car_fuel_system', 'car_tank_capacity',
                    'car_power','car_seating_capacity', 'car_standard_transmission', 'car_body_type', 'car_drive', 'car_wheelbase')
    actions = [export_to_csv]

class CustomerAdmin(admin.ModelAdmin):
    list_display =('customer_id', 'customer_name', 'customer_phone', 'customer_address', 'customer_birthday', 'customer_occupation', 'customer_gender')
    actions = [export_to_csv]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_id', 'store_name', 'store_address', 'store_phone', 'store_city', 'store_state')
    actions = [export_to_csv]

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_create_date', 'order_pickup_date', 'order_pickup_store', 'pickup_store_name', 'pickup_store_address', 'pickup_store_phone', 'pickup_store_city',
                    'pickup_store_state', 'order_return_date', 'order_return_store', 'return_store_name', 'return_store_address', 'return_store_phone', 'return_store_city', 'return_store_state')
    actions = [export_to_csv]

admin.site.register(Car, CarAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Order, OrderAdmin)
