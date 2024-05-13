from django.contrib import admin
from .models import Team



@admin.register(Team)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }