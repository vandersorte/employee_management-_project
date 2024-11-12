from django import forms
from django.core.exceptions import ValidationError
from .models import Funcioarios

class FuncionariosForm(forms.Form):
  #opções de cidades no Brasil
  CITY_CHOICES = (
    ('AC','Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
    ('DF', 'Distrito Federal'),
  )

  CITY_CHOICES = (
  ('Acre'),
  ('Alagoas'),
  ('Amapá'),
  ('Amazonas'),
  ('Bahia'),
  ('Ceará'),
  ('Espírito Santo'),
  ('Goiás'),
  ('Maranhão'),
  ('Mato Grosso'),
  ('Mato Grosso do Sul'),
  ('Minas Gerais'),
  ('Pará'),
  ('Paraíba'),
  ('Paraná'),
  ('Pernambuco'),
  ('Piauí'),
  ('Rio de Janeiro'),
  ('Rio Grande do Norte'),
  ('Rio Grande do Sul'),
  ('Rondônia'),
  ('Roraima'),
  ('Santa Catarina'),
  ('São Paulo'),
  ('Sergipe'),
  ('Tocantins'),
  ('Distrito Federal'),
)

  CARGOS_CHOICES = (
    ('Senior'),
    ('Pleno'),
    ('Junior'),
    ('Estágiario'),
  )

  FAIXAS_SALARIAIS = {
      'Senior': (10000, 20000),
      'Pleno': (6000, 9999),
      'Junior': (2000, 3000),
      'Estágiario': (1000, 1500),
  }

  # validação para que os campos númericos recebam apenas números
  def validate_number(value):
    if not value.isdigit():
        raise ValidationError('Deve conter apenas números')
    
  nome = forms.CharField('Nome', max_length=100)
  sobrenome = forms.CharField('Sobrenome', max_length=100)
  nascimento = forms.DateField('Nascimento')
  cpf = forms.CharField('CPF', max_length=14, default='')
  naturalidade = forms.CharField('Naturalidade',max_length=100, choices= CITY_CHOICES)
  remuneracao = forms.CharField('Remuneração',max_length=100, validators=[validate_number], default='')