from django.contrib import admin
from .models import Funcioarios

@admin.register(Funcioarios)
class FuncioariosAdmin(admin.ModelAdmin):
  list_display = ('nome', 'sobrenome', 'cargo')