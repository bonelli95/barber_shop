from django.shortcuts import render
from barber_shop.models import Fotografia

def index(request):
    fotografias = Fotografia.OPCOES_FOTOS
    return render(request, 'barber_shop/index.html', {'fotografias': fotografias})

def serviços(request):
    return render(request, 'barber_shop/serviços.html')
    
def imagens(request):
    categoria = request.GET.get('tipo')
    if categoria:
        fotografia = Fotografia.objects.filter(categoria=categoria)
    else:
        fotografia = Fotografia.objects.all()
    return render(request, 'barber_shop/imagens.html', {'fotografia': fotografia})

def contactos(request):
    return render(request, 'barber_shop/contactos.html')

