#Bibliotecas importantes

from django import forms
from .models import Team

#---------------------------------------------------------

class TeamModelForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'state', 'asc', 'creator', 'membros', 'supervisor']
        widgets = {
            'asc': forms.Select(attrs={'class': 'browser-default'}),  
            'membros': forms.Select(attrs={'class': 'browser-default'}),  
            'creator': forms.Select(attrs={'class': 'browser-default'}),  
            'supervisor': forms.Select(attrs={'class': 'browser-default'}),  
        }