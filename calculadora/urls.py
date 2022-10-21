from django.contrib import admin
from django.urls import path, include
from calculadora.views import home

urlpatterns = [

    path('', home)
]