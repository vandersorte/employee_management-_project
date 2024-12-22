from django import forms
from django.core.exceptions import ValidationError
from .models import Funcionarios

class FuncionariosForm(forms.ModelForm):
  class Meta:
    model = Funcionarios
    fields = '__all__'

class BuscarForm(forms.Form):
  nome = forms.CharField(label='Nome do Funcionário', max_length=100)
