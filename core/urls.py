from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('cadastro/', views.CadastroView, name='cadastro'),
    # path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('dados/', DadosView.as_view(), name='dados'),
]
