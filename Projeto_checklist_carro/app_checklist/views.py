from django.shortcuts import render
from .models import UsuarioTeste 

def cadastrar(request):
    mensagem = ""
    if request.method == "POST":
        v_matricula = request.POST.get("matricula")
        v_km = request.POST.get("km")
        v_usuario = request.POST.get("usuario")
        v_modelo = request.POST.get("modelo")
        v_placa = request.POST.get("placa")
        v_agua = request.POST.get("agua")
        v_combustivel = request.POST.get("combustivel")
        v_oleo = request.POST.get("oleo")

        novo_usuario = UsuarioTeste(usuario=v_usuario, km= v_km, matricula=v_matricula, placa = v_placa, modelo = v_modelo, agua = v_agua, combustivel = v_combustivel, oleo = v_oleo)
        novo_usuario.save()
        
        mensagem = f"Checklist cadastrado com sucesso!"

    return render(request, "teste.html", {"mensagem": mensagem})