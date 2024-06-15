# Library requires
from django import forms 
from .models import Projecto


class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Projecto
        fields = ['tipo', 'equipe', 'LV']
        widgets = {
            'tipo':forms.Select(attrs={'class':'browser-default'}),
            'equipe':forms.Select(attrs={'class':'browser-default'}),
            'LV':forms.Select(attrs={'class':'browser-default'}),
            # 'perfil':forms.Select(attrs={'class':'browser-default'}),
        }
        labels = {
            'tipo': 'Selecione o tipo de Projecto:',
            'equipe': 'Selecione a equipe correspondente:',
            'LV': 'Selecione o LV correspondente:',

        }

     

