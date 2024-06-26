# Lib Section 
# Only for Libs
from django.contrib.gis.db import models
from Accounts.models import ASC
from Team.models import Team
#-----------------------------------------------------------------------------

class PostoDeTransformao(models.Model):
    geom = models.PointField(blank=True, null=True)
    id_0 = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict.
    pt_number = models.CharField(db_column='PT NUMBER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    latittude = models.FloatField(db_column='Latittude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Posto de Transformação '

    def __str__(self):
        return self.pt_number

class PT(models.Model):
    PT_NUMBER = models.CharField(max_length=20)
    asc = models.ForeignKey (ASC, on_delete=models.CASCADE)


    def __str__(self):
        return self.PT_NUMBER
    

class LV_Feeder(models.Model):
    name = models.CharField(max_length=15)
    PT = models.ForeignKey(PostoDeTransformao, on_delete=models.CASCADE, related_name='saidas', null=True)


    def save(self, *args, **kwargs):
        if self.PT:
            pt_number = self.PT.pt_number
            self.name = f'{self.name}-{pt_number}'
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
    

class Project_type(models.Model):

    Project_TYPE = (
        ('Novo Levantamento', 'Novo Levantamento'),
        ('Novo PT Feeder ', 'Novo PT Feeder '),
        ('Levantamento Correction', 'Levantamento Correction'),
        ('Premisses Locked', ' Premisses Locked'),
    )

    type = models.CharField(max_length=30, choices=Project_TYPE, unique=True)

    def is_project_new(self):
        return self.type == ' Novo Levantamento'

    def is_project_feeder(self):
        return self.type == 'Novo PT Feeder'

    def is_project_correcao(self):
        return self.type == 'Levantamento Correction'
    
    def is_project_pl(self):
        return self.type == 'Premisses Locked'
    
    def __str__(self):
        return self.get_type_display()


class Projecto(models.Model):
    tipo = models.ForeignKey(Project_type, on_delete=models.CASCADE, default=1)
    equipe = models.ForeignKey(Team, on_delete=models.CASCADE, default=1)
    LV = models.ForeignKey(LV_Feeder, on_delete=models.CASCADE, default=1)
    # perfil = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['equipe'] 

    #Metodo para juntar dois campos de fields
    @property
    def lv_equipe_name(self):
        return f'{self.LV} - {self.equipe}'

    def __str__(self):
        return self.lv_equipe_name


    
    

    



    
    



