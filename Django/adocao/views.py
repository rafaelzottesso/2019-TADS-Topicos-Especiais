from django.shortcuts import render

# Importa todas as classes do models.py
from .models import Animal, Cidade, Estado, Raca, Tipo

# Importa função que vai chamar as urls pelo "name" delas
from django.urls import reverse_lazy

# Importar as classes Views para inserir, alterar e excluir utilizando formulários
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Importa o TemplateView para criação de páginas simples
from django.views.generic import TemplateView

# Importa ListView para gerar as telas com tabelas
from django.views.generic.list import ListView

# Importa o Mixin para obrigar login
from django.contrib.auth.mixins import LoginRequiredMixin


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

class EstadoCreate(LoginRequiredMixin, CreateView):
    # Define qual o modelo pra essa classe vai criar o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "adocao/formulario.html"
    # Pra onde redirecionar o usuário depois de inserir um registro. Informe o nome da url
    success_url = reverse_lazy("listar-estados")
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


class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-cidades")
    fields = ['nome', 'estado', 'descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(CidadeCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novas Cidades"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


class TipoCreate(LoginRequiredMixin, CreateView):
    model = Tipo
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-tipos")
    fields = ['descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(TipoCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novos Tipos"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


class RacaCreate(LoginRequiredMixin, CreateView):
    model = Raca
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-racas")
    fields = ['descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(RacaCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novas Raças"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


class AnimalCreate(LoginRequiredMixin, CreateView):
    model = Animal
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-animais")
    fields = ['tipo', 'raca', 'descricao',
              'nome', 'idade', 'cidade', 'telefone']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(AnimalCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novos Animais"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context

##################### EDITAR ######################


class EstadoUpdate(LoginRequiredMixin, UpdateView):
    # Define qual o modelo pra essa classe vai criar o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "adocao/formulario.html"
    # Pra onde redirecionar o usuário depois de editar um registro. Informe o nome da url
    success_url = reverse_lazy("listar-estados")
    # Quais campos devem aparecer no formulário?
    fields = ['sigla', 'nome']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(EstadoUpdate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Editar cadastro de Estado"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"

        # Devolve/envia o context para seu comportamento padrão
        return context


class CidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-cidades")
    fields = ['nome', 'estado', 'descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(CidadeUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Cidade"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context


class TipoUpdate(LoginRequiredMixin, UpdateView):
    model = Tipo
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-tipos")
    fields = ['descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(TipoUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Tipo"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context


class RacaUpdate(LoginRequiredMixin, UpdateView):
    model = Raca
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-racas")
    fields = ['descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(RacaUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Raça"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context


class AnimalUpdate(LoginRequiredMixin, UpdateView):
    model = Animal
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-animais")
    fields = ['tipo', 'raca', 'descricao',
              'nome', 'idade', 'cidade', 'telefone']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(AnimalUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Animal"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-primary"
        return context

##################### Excluir ######################


class EstadoDelete(LoginRequiredMixin, DeleteView):
    # Define qual o modelo pra essa classe vai criar o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "adocao/formulario.html"
    # Pra onde redirecionar o usuário depois de excluir um registro. Informe o nome da url
    success_url = reverse_lazy("listar-estados")

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

class CidadeDelete(LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-cidades")

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class TipoDelete(LoginRequiredMixin, DeleteView):
    model = Tipo
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-tipos")

    def get_context_data(self, *args, **kwargs):
        context = super(TipoDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class RacaDelete(LoginRequiredMixin, DeleteView):
    model = Raca
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-racas")

    def get_context_data(self, *args, **kwargs):
        context = super(RacaDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class AnimalDelete(LoginRequiredMixin, DeleteView):
    model = Animal
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-animais")

    def get_context_data(self, *args, **kwargs):
        context = super(AnimalDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

##################### Listar ######################

# Vai gerar uma tela com uma lista de estados


class EstadoList(LoginRequiredMixin, ListView):
    # Inform qual o modelo
    model = Estado
    # E o template
    template_name = "adocao/listas/list_estado.html"

class CidadeList(LoginRequiredMixin, ListView):
    model = Cidade
    template_name = "adocao/listas/list_cidade.html"

class TipoList(LoginRequiredMixin, ListView):
    model = Tipo
    template_name = "adocao/listas/list_tipo.html"

class RacaList(LoginRequiredMixin, ListView):
    model = Raca
    template_name = "adocao/listas/list_raca.html"

class AnimalList(LoginRequiredMixin, ListView):
    model = Animal
    template_name = "adocao/listas/list_animal.html"
