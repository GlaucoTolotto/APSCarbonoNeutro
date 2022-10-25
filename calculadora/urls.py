from django.urls import path
from calculadora.views import home, quemSomos

urlpatterns = [
    path('', home),
    path(r'^quemSomos/', quemSomos, name='quemSomos'),
]