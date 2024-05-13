from django.db import models
from Accounts.models import ASC
from Team.models import Team
# Create your models here.

#Analisar bem o nome da classe
class Estado(models.Model):

    Estado_TYPE = (
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('submetido', 'Submetido'),
        ('reijeitado', 'Reijeitado'),
    )

    status = models.CharField(max_length=15, choices=Estado_TYPE, unique=True)
    
    def is_pendente(self):
        return self.status == 'pendente'
    
    def is_aprovado(self):
        return self.status == 'aprovado'
    
    def is_submetido(self):
        return self.status == 'submetido'
    
    def is_reijeitado (self):
        return self.status == 'reijeitado'
    

    def __str__(self):
        return f'Estado - {self.status}'
    

class PT(models.Model):
    PT_NUMBER = models.CharField(max_length=20)
    asc = models.ForeignKey (ASC, on_delete=models.CASCADE)


    def __str__(self):
        return self.PT_NUMBER
    

class LV_Feeder(models.Model):
    name = models.CharField(max_length=15)
    PT = models.ManyToManyField (PT)


    def save(self, *args, **kwargs):
        if not self.name.startswith('PT'):
            raise ValueError("O nome do LV Feeder deve começar com 'PT'.")
        
        if '-' not in self.name:
            raise ValueError("O nome do LV Feeder deve incluir um traço (-) após 'PT'.")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
    

class Project_type(models.Model):

    Project_TYPE = (
        ('project_new', 'Projecto - Novo Levantamento'),
        ('project_feeder', 'Projecto - Novo PT Feeder '),
        ('project_correcao', 'Projecto - Levantamento Correcao'),
        ('project_pl', 'Projecto - Premisses Locked'),
    )

    type = models.CharField(max_length=30, choices=Project_TYPE, unique=True)

    def is_project_new(self):
        return self.type == 'project_new'

    def is_project_feeder(self):
        return self.type == 'project_feeder'

    def is_project_correcao(self):
        return self.type == 'project_correcao'
    
    def is_project_pl(self):
        return self.type == 'project_pl'
    
    def __str__(self):
        return self.type


class Projecto(models.Model):
    tipo = models.ForeignKey(Project_type, on_delete=models.CASCADE, default=1)
    equipe = models.ForeignKey(Team, on_delete=models.CASCADE, default=1)
    LV = models.ForeignKey(LV_Feeder, on_delete=models.CASCADE, default=1)
    perfil = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.LV} {self.equipe}'







    
    

    



    
    



