from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('cadastro/', views.CadastroView, name='cadastro'), # FBV (FUNCTIONS BASED VIEWS)
    # path('cadastro/', CadastroView.as_view(), name='cadastro'), # CBV (CLASS BASED VIEWS)
    # path('dados/', DadosView.as_view(), name='dados'),
    path('dados/', views.DadosView, name='dados'),
]
