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

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(EstadoCreate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Cadastro de novos Estados"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        # Devolve/envia o context para seu comportamento padrão
        return context

##################### EDITAR ######################

class EstadoUpdate(UpdateView):
    # Define qual o modelo pra essa classe vai criar o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "adocao/formulario.html"
    # Pra onde redirecionar o usuário depois de editar um registro. Informe o nome da url
    success_url = reverse_lazy("index")
    # Quais campos devem aparecer no formulário?
    fields = ['sigla', 'nome']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(EstadoUpdate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Alterar cadastro de Estado"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"

        # Devolve/envia o context para seu comportamento padrão
        return context


##################### Excluir ######################

class EstadoDelete(DeleteView):
    # Define qual o modelo pra essa classe vai criar o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "adocao/formulario.html"
    # Pra onde redirecionar o usuário depois de excluir um registro. Informe o nome da url
    success_url = reverse_lazy("index")

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(EstadoDelete, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        # Devolve/envia o context para seu comportamento padrão
        return context