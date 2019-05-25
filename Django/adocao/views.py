from django.shortcuts import render

# Importa todas as classes do models.py
from .models import *

# Importa função que vai chamar as urls pelo "name" delas
from django.urls import reverse_lazy

# Importar as classes Views para inserir, alterar e excluir utilizando formulários
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Importa o TemplateView para criação de páginas simples
from django.views.generic import TemplateView


# Create your views here.

# Cria uma classe com herança de TemplateView para exibir
# um arquivo HTML normal (com o conteúdo dele)
class PaginaInicialView(TemplateView):
    # Nome do arquivo que vai ser utilizado para renderizar
    # esta página/método/classe
    template_name = "adocao/index.html"

# Página "Sobre"


class SobreView(TemplateView):
    template_name = "adocao/sobre.html"

# Página de contato


class ContatoView(TemplateView):
    template_name = "adocao/contato.html"

# Página de Currículo


class CurriculoView(TemplateView):
    template_name = "adocao/curriculo.html"


##################### INSERIR ######################

class EstadoCreate(CreateView):
    # Define qual o modelo pra essa classe vai criar o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "adocao/formulario.html"
    # Pra onde redirecionar o usuário depois de inserir um registro. Informe o nome da url
    success_url = reverse_lazy("index")
    # Quais campos devem aparecer no formulário?
    fields = ['sigla', 'nome']


##################### EDITAR ######################

class EstadoUpdate(UpdateView):
    # Define qual o modelo pra essa classe vai criar o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "adocao/formulario.html"
    # Pra onde redirecionar o usuário depois de inserir um registro. Informe o nome da url
    success_url = reverse_lazy("index")
    # Quais campos devem aparecer no formulário?
    fields = ['sigla', 'nome']
