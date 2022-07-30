from msilib.schema import DuplicateFile
from pyexpat import model
from sqlite3 import DateFromTicks
from django.db import models

# Create your models here.

class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images')
    end_of_certificate = models.DateField(default=0000-00-00)
    end_of_drivers_license = models.DateField(default=0000-00-00)
    end_of_hygiene_license = models.DateField(default=0000-00-00)
    end_of_smart_license = models.DateField(default=0000-00-00)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

# class Bogey(models.Model):
#     slug = models.SlugField(unique=True)

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField()
#     access_level = models.CharField()

class Truck(models.Model):
    end_of_insurance = models.DateField(default=0000-00-00)
    end_of_technical_inspection = models.DateField(default=0000-00-00)
