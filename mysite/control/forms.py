from django import forms
from .models import Jornada

class JornadaForm(forms.ModelForm):
    class Meta:
        model = Jornada
        fields = ('empleado', 'fecha', 'tipo_marcacion')
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
