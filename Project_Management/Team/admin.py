from django.contrib import admin
from .models import Team



@admin.register(Team)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

#@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    
    # Adicione permissões personalizadas se necessário
    def has_view_permission(self, request, obj=None):
        return request.user.has_perm('Team.view_team')

    def has_add_permission(self, request):
        return request.user.has_perm('Team.add_team')

    def has_change_permission(self, request, obj=None):
        return request.user.has_perm('Team.change_team')

    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm('Team.delete_team')