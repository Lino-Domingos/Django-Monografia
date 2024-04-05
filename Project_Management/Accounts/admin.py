from django.contrib import admin
from .models import TipoUsuario, ASC, Usuario, Provincia, Direccao_Regional

# Registrar os modelos para serem exibidos na interface de administração
admin.site.register(TipoUsuario)
admin.site.register(ASC)
admin.site.register(Usuario)
admin.site.register(Provincia)
admin.site.register(Direccao_Regional)
