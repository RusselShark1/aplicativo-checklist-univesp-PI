from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .models import UsuarioTeste 

def fazer_login(request):
    mensagem = ""
    if request.method == "POST":
        u = request.POST.get("usuario")
        p = request.POST.get("senha")
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('dashboard')
            return redirect('cadastrar')
        else:
            mensagem = "Usuário ou senha incorretos."
    return render(request, "login.html", {"mensagem": mensagem})


def deslogar(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    if not request.user.is_superuser:
        return redirect('cadastrar')
    
    
    checklists = UsuarioTeste.objects.all().order_by('-id')
    return render(request, "dashboard.html", {"checklists": checklists})

@login_required
def mudar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'mudar_senha.html', {'form': form, 'sucesso': True})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'mudar_senha.html', {'form': form})

# 5. FORMULÁRIO DE CHECKLIST (COM VÍNCULO AUTOMÁTICO)
@login_required
def cadastrar(request):
    mensagem = ""
    if request.method == "POST":

        v_matricula = request.POST.get("matricula")
        v_km = request.POST.get("km")
        v_modelo = request.POST.get("modelo")
        v_placa = request.POST.get("placa")
        v_agua = request.POST.get("agua")
        v_combustivel = request.POST.get("combustivel")
        v_oleo = request.POST.get("oleo")
        v_frente = request.FILES.get("frente")
        v_traseira = request.FILES.get("traseira")
        v_motorista = request.FILES.get("motorista")
        v_passageiro = request.FILES.get("passageiro")
        v_avaria = request.POST.get("avaria_detalhes")
        v_foto_avaria = request.FILES.get("foto_avaria")

       
        novo_registro = UsuarioTeste(
            usuario=request.user, # O Django identifica o ID do motorista sozinho
            km=v_km, 
            matricula=v_matricula, 
            placa=v_placa, 
            modelo=v_modelo, 
            agua=v_agua, 
            combustivel=v_combustivel, 
            oleo=v_oleo,
            foto_frente=v_frente, 
            foto_traseira=v_traseira,
            foto_motorista=v_motorista, 
            foto_passageiro=v_passageiro,
            avaria_detalhes=v_avaria,
            foto_avaria=v_foto_avaria,
           
        )
        novo_registro.save()
        mensagem = "Checklist enviado com sucesso!"

    return render(request, "teste.html", {"mensagem": mensagem})