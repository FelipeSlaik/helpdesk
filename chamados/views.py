from django.shortcuts import render, redirect
from .models import Ticket

def lista_chamados(request):
    chamados = Ticket.objects.all()
    return render(request, 'chamados/lista.html', {'chamados': chamados})

def novo_chamado(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        prioridade = request.POST.get('prioridade')

        Ticket.objects.create(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade
        )

        return redirect('/chamados/')
    
    return render(request, 'chamados/novo.html')

def excluir_chamado(request, id):
    chamado = Ticket.objects.get(id=id)
    chamado.delete()

    return redirect('/chamados/')