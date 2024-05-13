# Bibliotecas Necessarias
from django.db import models
from Accounts.models import ASC, User
from django.utils import timezone
from django.template.defaultfilters import slugify
#---------------------------------------------------

  
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(default="", null=False)
    #state = models.ForeignKey(State, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    asc = models.ForeignKey(ASC, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_teams')
    membros = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams_members', limit_choices_to={'user_type__in':['tecnico_campo']}, default=1)
    membros_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams_members_1', limit_choices_to={'user_type__in':['tecnico_campo']}, default=1)
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams_supervisor', limit_choices_to={'user_type__in':['supervisor_campo']}, default=1)
    date_created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)  # Convertendo o nome para slug ao salvar
        super().save(*args, **kwargs)

    def __str__(self):
       return f'{self.name}'
    


