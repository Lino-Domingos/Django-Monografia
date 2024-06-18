from django.contrib import admin
from .models import  LV_Feeder, Projecto, Project_type
# Register your models here.

# admin.site.register(Estado)

class Projectosadmin(admin.ModelAdmin):
    list_display = ('equipe','tipo', 'LV', 'is_active')

admin.site.register(LV_Feeder)
admin.site.register(Projecto, Projectosadmin)
admin.site.register(Project_type)

