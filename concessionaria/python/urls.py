from django.urls import path
from . import views

urlpatterns = [
    # URL para listar carros disponíveis
    path('carros/', views.listar_carros, name='listar_carros'),
    # URL para registrar uma venda
    path('registrar_venda/', views.registrar_venda, name='registrar_venda'),
]
