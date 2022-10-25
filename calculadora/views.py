from django.shortcuts import render

def home(request):
    return render(request, 'calculadora/pages/home.html')


def desenvolvedores(request):
    return render(request, 'calculadora/pages/desenvolvedores.html')