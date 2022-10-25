from django.shortcuts import render

def home(request):
    return render(request, 'calculadora/pages/home.html')


def quemSomos(request):
    return render(request, 'calculadora/pages/quemSomos.html')