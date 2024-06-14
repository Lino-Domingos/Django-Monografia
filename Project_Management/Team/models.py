# Lib Section 
# Only for Libs
from django.db import models
from Accounts.models import ASC, User
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
#-----------------------------------------------------------------------------


# Team model:
# 
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(default="", null=False)
    #state = models.ForeignKey(State, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    asc = models.ForeignKey(ASC, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_teams')
    membros = models.ManyToManyField(User,  related_name='teams_members', limit_choices_to={'user_type__in':['tecnico_campo']})
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams_supervisor', limit_choices_to={'user_type__in':['supervisor_campo']}, default=1)
    date_created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
   
    def __str__(self):
       return f'{self.name}'
    
   
    def get_membros(self):
        return ", ".join([membro.first_name for membro in self.membros.first_name.all()])
    get_membros.short_description = 'Membros'
    


