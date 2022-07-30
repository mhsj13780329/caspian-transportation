from django.contrib import admin

# Register your models here.

from .models import Driver, Truck

admin.site.register(Driver)
admin.site.register(Truck)