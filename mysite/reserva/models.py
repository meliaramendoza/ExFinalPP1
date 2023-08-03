# reserva/models.py
from django.db import models

class Hotel(models.Model):
    identificador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

class Reserva(models.Model):
    identificador = models.AutoField(primary_key=True)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    numero_huespedes = models.PositiveIntegerField()
    tipo_habitacion = models.CharField(max_length=100)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado_reserva = models.CharField(max_length=20)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
