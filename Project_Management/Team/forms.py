# Library requires
from django import forms

from Accounts.models import User
from .models import Team


#---------------------------------------------------------
class TeamModelForm(forms.ModelForm):
    membros = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(user_type__in=['tecnico_campo']),
        widget=forms.SelectMultiple(attrs={'class': 'browser-default custom-select-multiple'})
    )
     
    class Meta:
        model = Team
        fields = ['name', 'asc', 'membros', 'supervisor']
        widgets = {
            'asc': forms.Select(attrs={'class': 'browser-default'}),  
            #'membros': forms.SelectMultiple(attrs={'class': 'browser-default custom-select-multiple'}),  
            # 'creator': forms.Select(attrs={'class': 'browser-default'}),  
            'supervisor': forms.Select(attrs={'class': 'browser-default'}),  
        }
        labels = {
            'name': 'Nome da Equipe',  # Exemplo de mudança de rótulo para o campo 'name'
            'asc': 'Selecione a Área de serviço ao Cliente-ASC',               # Exemplo de mudança de rótulo para o campo 'asc'
            'membros': 'Membros da Equipe',  # Exemplo de mudança de rótulo para o campo 'membros'
            'supervisor': 'Selecione o Supervisor de campo',  # Exemplo de mudança de rótulo para o campo 'supervisor'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
             # Filtrar o queryset para incluir apenas usuários que não estão em nenhuma equipe
        self.fields['membros'].queryset = User.objects.filter(user_type='tecnico_campo').exclude(teams_members__isnull=False)
        self.fields['membros'].widget.attrs['data-max-options'] = 2

    def clean(self):
        cleaned_data = super().clean()
        membros = cleaned_data.get('membros')
        if membros and len(membros) > 2:
            self.add_error('membros', forms.ValidationError("Selecione no máximo 2 membros para a equipe."))
        return cleaned_data
    