from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Funcioarios
from faker import Faker
import random
from datetime import datetime

fake = Faker('pt-br')

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

class CadastroView(TemplateView):
    template_name = 'cadastro_funcionarios.html'

    form_class = Funcioarios

    fun = Funcioarios.objects.all()
    fun.delete()

    # def gerar_funcionarios(quantidade):
    #     for _ in range(50):
    #         cargo = random.choice(tuple(CARGOS_CHOICES))
    #         remuneracao = random.randint(*FAIXAS_SALARIAIS[cargo])
    #         naturalidade = random.choice(tuple(CITY_CHOICES))
          
    #         Funcioarios.objects.create(
    #             nome = fake.first_name(),
    #             sobrenome = fake.last_name(),
    #             nascimento = fake.date_between_dates(date_start=datetime(1980,1,1), date_end=datetime(2005,12,31)),
    #             cpf = fake.cpf(),
    #             naturalidade = naturalidade,
    #             cargo = cargo,
    #             remuneracao = remuneracao,
    #         )
    # gerar = gerar_funcionarios(50)
    

class DadosView(TemplateView):
    template_name = 'dados_funcionarios.html'
    form_class = Funcioarios

    def get_context_data(self, **kwargs):
      context = super(DadosView, self).get_context_data(**kwargs)
      context['funcionarios'] = Funcioarios.objects.order_by().all()
      return context