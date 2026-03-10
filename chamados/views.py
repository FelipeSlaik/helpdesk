from django.shortcuts import render
from .models import Ticket

def lista_chamados(request):
    chamados = Ticket.objects.all()
    return render(request, 'chamados/lista.html', {'chamados': chamados})
