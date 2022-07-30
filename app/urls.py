from xml.etree.ElementInclude import include
from django.urls import path, include
from django.views.generic.base import TemplateView 
from . import views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('dashboard/', views.dashboard)  ,
    path('cars/', views.cars),
    path('drivers/', views.drivers, name='all-drivers'),
    path('drivers/<slug:driver_slug>', views.driver_details, name='driver-detail'),
    path('bogies/', views.bogies),
    path('trucks/', views.trucks)   
]