# cashflow/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
    path('adicionar_transacao/', views.adicionar_transacao, name='adicionar_transacao'),
    path('relatorios/', views.relatorios, name='relatorios'),
]