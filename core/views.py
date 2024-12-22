from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Funcionarios
from .forms import FuncionariosForm, BuscarForm
from faker import Faker
import random
from datetime import datetime
from django.contrib import messages

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

class HomeView(TemplateView):
  template_name = 'home.html'

class LoginView(TemplateView):
  template_name = 'login.html' 

def CadastroView(request):
  form = FuncionariosForm(request.POST or None)

  if str(request.method) == 'GET':
    context = {
        'form': FuncionariosForm
    }
    return render(request, 'cadastro.html', context)
  
  if str(request.method) == 'POST':
    if form.is_valid():
      form.save()
      context = {
        'form': FuncionariosForm,
      }
      messages.success(request, 'Dados salvos com sucesso.')
      form = FuncionariosForm()
      return render(request, 'cadastro_funcionarios.html', context)
  else:  
      messages.error(request, 'Erro, dados não poderam ser salvos.')
      context = {
        'form': FuncionariosForm,
      }
      return render(request, 'cadastro.html', context)

# DADOS FAKE
fake = Faker('pt-br')
def gerar_funcionarios(quantidade): # FUNÇÃO QUE GERA DADOS FAKE
    for _ in range(quantidade):
        cargo = random.choice(tuple(CARGOS_CHOICES))
        remuneracao = random.randint(*FAIXAS_SALARIAIS[cargo])
      
        Funcionarios.objects.create(
            nome = fake.first_name(),
            sobrenome = fake.last_name(),
            nascimento = fake.date_between_dates(date_start=datetime(1980,1,1), date_end=datetime(2005,12,31)),
            cpf = fake.cpf(),
            cargo = cargo,
            remuneracao = remuneracao,
        )
gerar_funcionarios(5)
# fun = Funcionarios.objects.all() 
# fun.delete() # FUNÇÃO PARA EXCLUIR OS DADOS FAKE 
# END DADOS FAKE    

def DadosView(request):
  context = {
     'dados': Funcionarios.objects.all()
  }
  
  return render(request, 'dados.html', context)