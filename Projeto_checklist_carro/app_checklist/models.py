from django.db import models
from django.contrib.auth.models import User 

class UsuarioTeste(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Motorista")
    
    matricula = models.IntegerField()
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    km = models.IntegerField()
    
    agua = models.CharField(max_length=10)
    oleo = models.CharField(max_length=10)
    combustivel = models.CharField(max_length=10)
    
    foto_frente = models.ImageField(upload_to='checklists/', null=True, blank=True)
    foto_traseira = models.ImageField(upload_to='checklists/', null=True, blank=True)
    foto_motorista = models.ImageField(upload_to='checklists/', null=True, blank=True)
    foto_passageiro = models.ImageField(upload_to='checklists/', null=True, blank=True)
    
    avaria_detalhes = models.TextField(max_length=500, null=True, blank=True)
    foto_avaria = models.ImageField(upload_to='checklists/avarias/', null=True, blank=True)
    
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.placa}"