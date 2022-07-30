from datetime import date, datetime
from enum import Flag
from http.client import HTTPResponse
import imp
from wsgiref.util import request_uri
from django.shortcuts import render

from app.models import Driver, Truck

# Create your views here.

def login(request):
    return render(request, 'app/login.html')

def dashboard(request):
    if(request.user.is_authenticated):
        user = request.user
        return render(request, 'app/dashboard.html', {
            'user' : user,
            'user_found': True
            })
    else:
        return render(request, 'app/login-error.html', {
            'user_found': False
        })

def drivers(request):

    if(request.user.is_authenticated): 
        drivers = Driver.objects.all()
        drivers_info = []
            
        current_date = datetime.now().date()
        drivers_license_alert = []
        for driver in drivers:
            diff = current_date - driver.end_of_drivers_license
            if diff.days < 20:
                drivers_license_alert.append(True)
            else:
                drivers_license_alert.append(False)
        for driver in drivers:
            new_driver = []
            driver_fist_name = driver.first_name
            driver_last_name = driver.last_name
            driver_image = driver.image
            driver_end_of_drivers_license = driver.end_of_drivers_license
            new_driver.append(driver_fist_name)
            new_driver.append(driver_last_name)
            new_driver.append(driver_image)
            new_driver.append(driver_end_of_drivers_license)
            drivers_info.append(new_driver)
            # new_driver.append(drivers_license_alert(driver.getIndex()))
        return render(request, 'app/drivers.html', {
            'drivers': drivers_info,
            'drivers_license_alert': drivers_license_alert
        })
    else:
        return render(request, 'app/login-error.html')

def bogies(request):
    return render(request, 'app/bogies.html')

def cars(request):
    return render(request, 'app/cars.html')

def driver_details(request, driver_slug):
    try:
        if request.user.is_authenticated:
            selected_driver = Driver.objects.get(slug=driver_slug)
            return render(request, 'app/driver-details.html', {
                'driver_found': True,
                'driver': selected_driver
            })
        else:
            return render(request, 'app/login-error.html')
    except Exception as exc:
        return render(request, 'app/driver-details.html', {
            'driver_found': False
        })

def trucks(request):
    if request.user.is_authenticated:
        trucks = Truck.objects.all()
        return render(request, 'app/trucks.html', {
            'trucks': trucks
        })
    else:
        return render(request, 'app/login-error.html')