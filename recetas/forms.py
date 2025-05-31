from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'categoria', 'ingredientes', 'preparacion', 
                 'tiempo_preparacion', 'dificultad', 'imagen']
        widgets = {
            'ingredientes': forms.Textarea(attrs={'rows': 5}),
            'preparacion': forms.Textarea(attrs={'rows': 10}),
        }

class BusquedaForm(forms.Form):
    query = forms.CharField(label='Buscar recetas', max_length=100)