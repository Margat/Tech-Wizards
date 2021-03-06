from django.db import models
from django.core.validators import RegexValidator

# Regex Validator to validate four digit year fields
year_validator = RegexValidator(
    regex='[0-9]{4}',
    message='Year must be a four digit number',
    code='Invalid year'
)

# Represents a Car and its fields in the database
class Car(models.Model):
    car_id = models.IntegerField(primary_key=True, default=0)
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_series = models.CharField(max_length=50)
    car_series_year = models.CharField(max_length=4, validators=[year_validator])
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

# Represents a Customer and its fields in the database
class Customer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    customer_id = models.IntegerField(primary_key=True, default=0)
    customer_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=50)
    customer_address = models.CharField(max_length=50)
    customer_birthday = models.CharField(max_length=50)
    customer_occupation = models.CharField(max_length=50)
    customer_gender = models.CharField(max_length = 6, choices=GENDER_CHOICES)
    def __str__(self):
        return self.customer_name

# Represents a Store and its fields in the database
class Store(models.Model):
    store_id = models.IntegerField(primary_key=True, default=0)
    store_name = models.CharField(max_length=50)
    store_address = models.CharField(max_length=50)
    store_phone = models.CharField(max_length=50)
    store_city = models.CharField(max_length=50)
    store_state = models.CharField(max_length=50)
    def __str__(self):
        return self.store_name

# Represents an ORder and its fields in the database
class Order(models.Model):
    order_id = models.IntegerField(primary_key=True, default=0)
    order_create_date = models.CharField(max_length=50)
    order_pickup_date = models.CharField(max_length=50)
    order_pickup_store = models.IntegerField()
    pickup_store_name = models.CharField(max_length=50)
    pickup_store_address = models.CharField(max_length=50)
    pickup_store_phone = models.CharField(max_length=50)
    pickup_store_city = models.CharField(max_length=50)
    pickup_store_state = models.CharField(max_length=50)
    order_return_date = models.CharField(max_length=50)
    order_return_store = models.IntegerField()
    return_store_name = models.CharField(max_length=50)
    return_store_address = models.CharField(max_length=50)
    return_store_phone = models.CharField(max_length=50)
    return_store_city = models.CharField(max_length=50)
    return_store_state = models.CharField(max_length=50)
