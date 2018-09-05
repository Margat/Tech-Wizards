from django.db import models

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    def __str__(self):
        return self.car_name
