from django.urls import path
from barber_shop.views import index

urlpatterns = [
    path('', index),
]
