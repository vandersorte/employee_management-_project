from django.urls import path
from .views import HomeView, LoginView, CadastroView, DadosView, RecursosView, ContatoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('dados/', DadosView.as_view(), name='dados'),
    path('recursos/', RecursosView.as_view(), name='recursos'),
    path('contato/', ContatoView.as_view(), name='contato'),
]
