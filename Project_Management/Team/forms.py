#Bibliotecas importantes

from django import forms
from .models import team

#---------------------------------------------------------

class TeamModelForm(forms.ModelForm):
    class Meta:
        model = team
        fields = ['name', 'state', 'asc','creator', 'membros', 'supervisor']
        widgets = {
            'asc': forms.Select(attrs={'class': 'browser-default'}),  
            'date_create': forms.DateTimeInput(attrs={'class': 'datepicker'}),  
            'membros': forms.Select(attrs={'class': 'browser-default'}),  
            'supervisor': forms.Select(attrs={'class': 'browser-default'}),  
        }