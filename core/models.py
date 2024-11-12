
from django.db import models
from django.core.exceptions import ValidationError

class Funcioarios(models.Model):
  
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

  CARGOS_CHOICES = (
    ('Estágio','Estágiário'),
    ('Jr', 'Junior'),
    ('Pl', 'Pleno'),
    ('Sr','Senior'),
    ('Tl', 'Tech Lead'),
  )

  # validação para que os campos númericos recebam apenas números
  def validate_number(value):
    if not value.isdigit():
        raise ValidationError('Deve conter apenas números')
    
  nome = models.CharField('Nome', max_length=100)
  sobrenome = models.CharField('Sobrenome', max_length=100)
  nascimento = models.DateField('Nascimento')
  cpf = models.CharField('CPF', max_length=14, default='')
  naturalidade = models.CharField('Naturalidade',max_length=100)
  cargo = models.CharField('Cargo', max_length=100)
  remuneracao = models.CharField('Remuneração',max_length=100, validators=[validate_number], default='')


  
  class Meta:
    verbose_name = 'Funcionario'
    verbose_name_plural = 'Funcionarios'

  def __str__(self) -> str:
    return self.nome
  
