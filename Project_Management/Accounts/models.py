from django.db import models
from django.contrib.auth.models import Group  # Importe o modelo Group do Djang
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Permission
from django.utils.translation import gettext as _


# Create your models here.

# Classe para o tipo de User
class TipoUsuario(models.Model):
    nome = models.CharField(max_length = 40)

    def __str__(self):
        return self.nome
    

  # Classe responsavel pela area de servico ao Cliente  
class ASC(models.Model):
    nome = models.CharField(max_length = 30)
    direccao_regional = models.CharField (max_length = 7)
    sigla_ASC = models.CharField(max_length = 2)

    def __str__(self):
        return self.nome
    
# Classe responsavel pelo usuario
    
class Usuario(AbstractUser):
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    ASC = models.ForeignKey(ASC, on_delete=models.CASCADE)

    # Adicione related_name para evitar colisões
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='team_user_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='team_user_permissions',
        help_text=_('Specific permissions for this user.'),
    )

   