from django import forms
from .models import Task, Projecto



class CreateForm(forms.ModelForm):
    # project = forms.ModelChoiceField(queryset=Projecto.objects.all())
    project = forms.ModelChoiceField(
         queryset=Projecto.objects.filter(is_active=True),
         empty_label="Selecione um projeto",
         widget=forms.Select(attrs={'class': 'browser-default'}),
    )
     
    class Meta:
        model = Task
        fields = ['name', 'project']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'project': forms.Select(attrs={'class': 'browser-default'}),
        }
    
    def clean_project(self):
        project = self.cleaned_data['project']
        if Task.objects.filter(project=project).exists():
            raise forms.ValidationError("Este projeto já está atribuído a uma tarefa.")
        return project

   
    