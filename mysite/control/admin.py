from django.contrib import admin
from .models import Empleado, Jornada
from .forms import JornadaForm

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento', 'turno', 'horario_entrada', 'horario_salida')
    list_filter = ('departamento', 'turno')

class JornadaAdmin(admin.ModelAdmin):
    form = JornadaForm
    list_display = ('empleado', 'fecha', 'tipo_marcacion')
    list_filter = ('tipo_marcacion', 'fecha')

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Jornada, JornadaAdmin)
