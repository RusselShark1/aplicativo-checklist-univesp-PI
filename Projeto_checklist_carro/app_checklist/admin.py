from django.contrib import admin
from .models import UsuarioTeste # Importa sua tabela

admin.site.register(UsuarioTeste) # Avisa o Django para mostrar essa tabela no Adminpython manage.py createsuperuser