from django.urls import path
from barber_shop.views import index, serviços, imagens

urlpatterns = [
    path('', index, name='index'),
    path('serviços/', serviços, name='serviços'),
    path('imagens/', imagens, name='imagens'),
]
