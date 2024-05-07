from django.urls import path
from barber_shop.views import index, serviços

urlpatterns = [
    path('', index, name='index'),
    path('serviços/', serviços, name='serviços'),
]
