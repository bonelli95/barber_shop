from django.shortcuts import render

def index(request):
    return render(request, 'barber_shop/index.html')

def serviços(request):
    return render(request, 'barber_shop/serviços.html')