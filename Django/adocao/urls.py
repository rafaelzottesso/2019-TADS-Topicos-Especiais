# módulo do Django para criar urls
from django.urls import path

# Importe todas suas classes do views.py
from .views import *

urlpatterns = [
    # path('caminho/da/url', ClasseLáDoView.as_view(), name="nomeDessaURL" )
    path('', PaginaInicialView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('contato/', ContatoView.as_view(), name="contato"),
    path('curriculo/', CurriculoView.as_view(), name="curriculo"),

    # URLS de cadastros
    path('cadastrar/estado/', EstadoCreate.as_view(), name="cadastrar-estado"),
    
    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
    
]
