from django.contrib import admin
from .models import Team
from django.core.exceptions import ValidationError



#@admin.register(Team)
# class AuthorAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',), }

class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    list_display = ('name','state', 'asc', 'creator', 'get_membros', 'date_created')
    exclude = ('creator',)  # Excluir o campo 'creator' do formulário

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set the creator during the first save.
            obj.creator = request.user
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        obj = form.instance
        for membro in form.cleaned_data['membros']:
            obj.membros.add(membro)

    def get_membros(self, obj):
        return ", ".join([membro.first_name for membro in obj.membros.all()])
    get_membros.short_description = 'Membros'

admin.site.register(Team, TeamAdmin)


    