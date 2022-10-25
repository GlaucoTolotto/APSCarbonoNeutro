from django.urls import path
from calculadora.views import home, desenvolvedores

urlpatterns = [
    path('', home, name=''),
    path('desenvolvedores/', desenvolvedores, name='desenvolvedores'),
]