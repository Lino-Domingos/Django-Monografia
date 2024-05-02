#Bibliotecas importantes

from django import forms
from .models import team

#---------------------------------------------------------

class TeamModelForm(forms.ModelForm):
    class Meta:
        model = team
        fields = ['name', 'state', 'asc','creator', 'membros', 'supervisor']
        widgets = {
            'asc': forms.Select(attrs={'class': 'browser-default'}),  # Exemplo de renderização de um campo ForeignKey como um menu suspenso
            'date_create': forms.DateTimeInput(attrs={'class': 'datepicker'}),  # Exemplo de renderização de um campo DateTimeField como um campo de data e hora
            'creator': forms.Select(attrs={'class': 'browser-default'}),  # Exemplo de renderização de um campo ForeignKey como um menu suspenso
            'membros': forms.Select(attrs={'class': 'browser-default'}),  # Exemplo de renderização de um campo ForeignKey como um menu suspenso
            'supervisor': forms.Select(attrs={'class': 'browser-default'}),  # Exemplo de renderização de um campo ForeignKey como um menu suspenso
        }