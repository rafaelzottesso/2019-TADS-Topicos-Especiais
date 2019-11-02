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

    # URLS de Estado
    path('cadastrar/estado/', EstadoCreate.as_view(), name="cadastrar-estado"),
    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name="excluir-estado"),
    path('listar/estados/', EstadoList.as_view(), name="listar-estados"),

    # URLS de Cidade
    path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name="excluir-cidade"),
    path('listar/cidade/', CidadeList.as_view(), name="listar-cidades"),

    # URLS de Tipo
    path('cadastrar/tipo/', TipoCreate.as_view(), name="cadastrar-tipo"),
    path('editar/tipo/<int:pk>/', TipoUpdate.as_view(), name="editar-tipo"),
    path('excluir/tipo/<int:pk>/', TipoDelete.as_view(), name="excluir-tipo"),
    path('listar/tipo/', TipoList.as_view(), name="listar-tipos"),

    # URLS de Raca
    path('cadastrar/raca/', RacaCreate.as_view(), name="cadastrar-raca"),
    path('editar/raca/<int:pk>/', RacaUpdate.as_view(), name="editar-raca"),
    path('excluir/raca/<int:pk>/', RacaDelete.as_view(), name="excluir-raca"),
    path('listar/raca/', RacaList.as_view(), name="listar-racas"),

    # URLS de Animal
    path('cadastrar/animal/', AnimalCreate.as_view(), name="cadastrar-animal"),
    path('editar/animal/<int:pk>/', AnimalUpdate.as_view(), name="editar-animal"),
    path('excluir/animal/<int:pk>/', AnimalDelete.as_view(), name="excluir-animal"),
    path('listar/animal/', AnimalList.as_view(), name="listar-animais"),
    path('ver/animal/<int:pk>/', AnimalDetalhes.as_view(), name="detalhar-animal"),

]
