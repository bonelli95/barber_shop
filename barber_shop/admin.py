from django.contrib import admin
from barber_shop.models import Fotografia

class listandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'foto')
    list_display_links = ('id', 'nome', 'foto')

admin.site.register(Fotografia, listandoFotografias)