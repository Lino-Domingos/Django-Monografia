# Lib Section 
# Only for Libs
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password 
#-----------------------------------------------------------------------------




#Provincias 
# Classe Provincia
class Provincia(models.Model):
    nome_provincia = models.CharField(max_length=50, default="Cidade de Maputo")


    def __str__(self):
        return self.nome_provincia


# ASC
class Direccao_Regional(models.Model):
     nome_direccao = models.CharField(max_length=10, null=True, blank=True)
     provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True, blank=True)

     def __str__(self):
          return self.nome_direccao
     

# Classe responsavel pela ASC  
class ASC(models.Model):
    nome = models.CharField(max_length = 30)
    codigo_ASC = models.CharField(max_length = 2)
    direccao_regional = models.ForeignKey(Direccao_Regional, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# Classe responsavel pelo Customizacao do usuario
class CustomUsuario(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username.strip(), email=email, **extra_fields)

        user.set_password(password)  
        user.save(using=self._db)

        return user


    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


# Classe responsavel do usuario
class User(AbstractUser):

    ASC = models.ForeignKey(ASC, on_delete=models.SET_NULL, null=True, blank=True)

    
#Tupla dos tipos de usuarios: Primeira Coluna armazenamento na Base de dados
    USER_TYPE_CHOICES = (
        ('tecnico_campo', 'Operador de Campo'),
        ('supervisor_campo', 'Supervisor de Campo'),
        ('tecnico_office', 'Tecnico Office'),
        ('supervisor_ASC', 'Supervisor ASC'),
        ('supervisor_regiao', 'Supervisor da Região'),
        ('direccao_central', 'Direcção Central'),

    )


# New Field User_Type
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    #As classes devem estar dentro do modelo personalizado simplesmente

#Chave Estrangeira ASC
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


#Function Inicializar os novos Campos
    def is_tecnico_campo(self):
        return self.user_type == 'tecnico_campo'

    def is_supervisor_campo(self):
        return self.user_type == 'supervisor_campo'

    def is_tecnico_office(self):
        return self.user_type == 'tecnico_office'
    
    def is_supervisor_ASC(self):
        return self.user_type == 'supervisor_ASC'
    
    def is_supervisor_regiao(self):
        return self.user_type == 'supervisor_regiao'
    
    def is_direccao_central(self):
        return self.user_type == 'direccao_central'



#Cria uma nova instancia CustomUsuario   
    objects = CustomUsuario()
