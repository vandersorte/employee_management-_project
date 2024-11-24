from django import forms
from django.core.exceptions import ValidationError
from .models import Funcioarios

class FuncionariosForm(forms.ModelForm):

  class Meta:
    model = Funcioarios
    fields = '__all__'
    
