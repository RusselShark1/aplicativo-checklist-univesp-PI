from django.db import models

class UsuarioTeste(models.Model):   
    usuario = models.CharField(max_length=100)
    matricula = models.IntegerField()
    km = models.IntegerField()
    modelo = models.CharField(max_length=100)
    oleo = models.CharField(max_length=100)
    agua = models.CharField(max_length=100)
    combustivel = models.CharField(max_length=100)
    placa = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario