# views.py
from django.shortcuts import render
from .models import ChecklistVeicular

# Linha 8: A definição da função
def salvar_checklist(request):
    # TUDO aqui dentro precisa de 4 espaços de recuo
    if request.method == 'POST':
        # TUDO aqui dentro do IF precisa de mais 4 espaços (total 8)
        re_val = request.POST.get('re_colaborador')
        nome_val = request.POST.get('nome_colaborador')
        modelo_val = request.POST.get('modelo_veiculo')
        placa_val = request.POST.get('placa_veiculo')

        ChecklistVeicular.objects.create(
            re=re_val,
            nome=nome_val,
            modelo=modelo_val,
            placa=placa_val
        )
        return render(request, 'sucesso.html') 
    
    # Este return volta para o alinhamento do IF
    return render(request, 'index.html')

# app_checklist/views.py

def home(request):
    if request.method == 'POST':
        # ... seu código de salvar aqui ...
        pass 
    return render(request, 'index.html')