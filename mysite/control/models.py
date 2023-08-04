from django.db import models

class Empleado(models.Model):
    TURNO_CHOICES = [
        ('Dia', 'Día'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
    ]

    identificador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    departamento = models.CharField(max_length=100)
    fecha_inicio = models.DateField(auto_now_add=True)
    dias_trabajo = models.CharField(max_length=100)
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES)
    horario_entrada = models.TimeField()
    horario_salida = models.TimeField()
    activo = models.BooleanField(default=True)  # Nuevo campo
    telefono = models.CharField(max_length=20, blank=True, null=True)  # Nuevo campo

    def __str__(self):
        return self.nombre


class Jornada(models.Model):
    TIPO_MARCACION_CHOICES = [
        ('Entrada', 'Entrada'),
        ('Salida', 'Salida'),
    ]

    identificador = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    tipo_marcacion = models.CharField(max_length=10, choices=TIPO_MARCACION_CHOICES)
