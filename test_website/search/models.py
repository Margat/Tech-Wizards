from django.db import models

# Create your models here.
class Car(models.Model):
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_series = models.CharField(max_length=50)
    car_series_year = models.IntegerField()
    car_price_new = models.IntegerField()
    car_engine_size = models.CharField(max_length=50)
    car_fuel_system = models.CharField(max_length=50)
    car_tank_capacity = models.CharField(max_length=50)
    car_power = models.CharField(max_length=50)
    car_seating_capacity = models.IntegerField()
    car_standard_transmission = models.CharField(max_length=50)
    car_body_type = models.CharField(max_length=50)
    car_drive = models.CharField(max_length=50)
    car_wheelbase = models.CharField(max_length=50)

    def __str__(self):
        return self.car_make + ' ' + self.car_model

class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_phone = models.IntegerField()
    customer_address = models.CharField(max_length=50)
    customer_birthday = models.DateField()
    customer_occupation = models.CharField(max_length=50)
    customer_gender = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name

class Store(models.Model):
    store_name = models.CharField(max_length=50)
    store_address = models.CharField(max_length=50)
    store_phone = models.IntegerField()
    store_city = models.CharField(max_length=50)
    store_state = models.CharField(max_length=50)

    def __str__(self):
        return self.store_name

class Order(models.Model):
    order_create_date = models.DateField()

    order_pickup_date = models.DateField()
    order_pickup_store = models.IntegerField()
    pickup_store_name = models.CharField(max_length=50)
    pickup_store_address = models.CharField(max_length=50)
    pickup_store_phone = models.IntegerField()
    pickup_store_city = models.CharField(max_length=50)
    pickup_store_state = models.CharField(max_length=50)

    order_return_date = models.DateField()
    order_return_store = models.IntegerField()
    return_store_name = models.CharField(max_length=50)
    return_store_address = models.CharField(max_length=50)
    return_store_phone = models.IntegerField()
    return_store_city = models.CharField(max_length=50)
    return_store_state = models.CharField(max_length=50)
