# models.py
from django.db import models

# Verifique se o nome aqui é exatamente este:
class ChecklistVeicular(models.Model): 
    re = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=10)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.placa

