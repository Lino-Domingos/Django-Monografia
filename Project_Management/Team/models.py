# Bibliotecas Necessarias
from django.db import models
from Accounts.models import ASC, User
#---------------------------------------------------

  
class team(models.Model):
    name = models.CharField(max_length=1, blank=True, null=True)
    #state = models.ForeignKey(State, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    asc = models.ForeignKey(ASC, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_teams')
    membros = models.ManyToManyField(User, related_name='teams_members', limit_choices_to={'user_type__in':['tecnico_campo']})
    supervisor = models.ManyToManyField(User, related_name='teams_supervisor', limit_choices_to={'user_type__in':['supervisor_campo']})
    date_create = models.DateTimeField(auto_now_add=True)


    def __str__(self):
       return f'Team - {self.id} {self.name}'
