from django.contrib import admin
from .models import *

@admin.register(NiveisAcesso)
class NivelAadmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('matricula','cpf','nome', 'departamento','nivel_acesso', 'password_hash')

@admin.register(Rotinas)
class RotinasaAdmin(admin.ModelAdmin):
    list_display = ('descricao_rotina','nivel_acesso')

@admin.register(Departamentos)
class DepartamentosAdmin(admin.ModelAdmin):
    list_display = ('nome_depart',)
