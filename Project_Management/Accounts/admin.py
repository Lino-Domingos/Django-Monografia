from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Importar os modelos criados
from .models import Direccao_Regional, ASC, Provincia, User

# Registrar os outros modelos
admin.site.register(Provincia)
admin.site.register(Direccao_Regional)
admin.site.register(ASC)



class CustomUserAdmin(BaseUserAdmin):
    # Campos que serão exibidos na página de administração no user Team
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Informações Adicionais', {'fields': ('user_type',)}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
        ('Area de Servico', {'fields': ('ASC',)}),
    )
    # Campos que serão exibidos na lista de usuários
    list_display = ('username', 'first_name', 'last_name', 'user_type','is_staff', 'ASC')

# Registrar o modelo de usuário personalizado com o UserAdmin personalizado
admin.site.register(User, CustomUserAdmin)