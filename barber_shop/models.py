from django.db import models

class Fotografia(models.Model):

    BARBEARIA = 'barbearia'
    CORTES = 'cortes'

    OPCOES_FOTOS = [
        (BARBEARIA, "Barbearia"),
        (CORTES, "Cortes"),
    ]

    titulo = models.CharField(max_length=50, null=False, blank=True, default="")
    nome = models.CharField(max_length=20, null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/", blank=True)
    categoria = models.CharField(max_length=20, choices=OPCOES_FOTOS, default="BARBEARIA")

    

    def __str__(self):
        return f'Fotografia [titulo={self.titulo}]'
    