from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Direccao_Regional, ASC, User, Provincia


# Registo das Tabelas ADMIN
admin.site.register(Direccao_Regional)
admin.site.register(Provincia)
admin.site.register(ASC)
admin.site.register(User)