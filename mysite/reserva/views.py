from django.shortcuts import render
from .models import Reserva

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reserva/listar_reservas.html', {'reservas': reservas})
