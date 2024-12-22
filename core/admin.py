from django.contrib import admin
from .models import Funcionarios

@admin.register(Funcionarios)
class FuncionariosAdmin(admin.ModelAdmin):
  list_display = ('nome', 'sobrenome', 'cargo')