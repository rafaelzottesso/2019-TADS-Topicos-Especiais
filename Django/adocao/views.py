from django.shortcuts import render

# Importa todas as classes do models.py
from .models import Animal, Cidade, Estado, Raca, Tipo

# Importa função que vai chamar as urls pelo "name" delas
from django.urls import reverse_lazy

# Importar as classes Views para inserir, alterar e excluir utilizando formulários
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Importa o TemplateView para criação de páginas simples
from django.views.generic import TemplateView

# Importa o DetailView para ver detalhes de objetos
from django.views.generic.detail import DetailView

# Importa ListView para gerar as telas com tabelas
from django.views.generic.list import ListView

# Importa o Mixin para obrigar login
from django.contrib.auth.mixins import LoginRequiredMixin

# Biblioteca para controlar o acesso por grupo de usuário
from braces.views import GroupRequiredMixin

# Método que busca um objeto. Se não existir, da um erro 404
from django.shortcuts import get_object_or_404

# Create your views here.

# Cria uma classe com herança de TemplateView para exibir
# um arquivo HTML normal (com o conteúdo dele)


class PaginaInicialView(TemplateView):
    # Nome do arquivo que vai ser utilizado para renderizar
    # esta página/método/classe
    template_name = "adocao/index.html"

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super().get_context_data(*args, **kwargs)

        # Listar somente os últimos 10 registros
        context['ultimos_animais'] = Animal.objects.all().reverse()[:10]

        return context

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

class EstadoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    # Define o grupo de usuário que pode acessar esta view
    group_required = u"Administrador"
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


class CidadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
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


class TipoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
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


class RacaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
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
              'nome', 'idade', 'foto', 'cidade', 'telefone']

    def form_valid(self, form):

        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        
        url = super().form_valid(form)

        return url

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(AnimalCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novos Animais"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context

##################### EDITAR ######################


class EstadoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
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


class CidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
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


class TipoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
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


class RacaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
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
              'nome', 'idade', 'foto', 'cidade', 'telefone']

    # Altera a query para buscar o objeto do usuário logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Animal, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(AnimalUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Animal"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-primary"
        return context

##################### Excluir ######################


class EstadoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
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

class CidadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    model = Cidade
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-cidades")

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class TipoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    model = Tipo
    template_name = "adocao/formulario.html"
    success_url = reverse_lazy("listar-tipos")

    def get_context_data(self, *args, **kwargs):
        context = super(TipoDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class RacaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
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

    # Altera a query para buscar o objeto do usuário logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Animal, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super(AnimalDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

##################### Listar ######################

# Vai gerar uma tela com uma lista de estados


class EstadoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    # Inform qual o modelo
    model = Estado
    # E o template
    template_name = "adocao/listas/list_estado.html"

class CidadeList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    model = Cidade
    template_name = "adocao/listas/list_cidade.html"

class TipoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    model = Tipo
    template_name = "adocao/listas/list_tipo.html"

class RacaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    model = Raca
    template_name = "adocao/listas/list_raca.html"

class AnimalList(LoginRequiredMixin, ListView):
    model = Animal
    template_name = "adocao/listas/list_animal.html"

    # Altera a query padrão para buscar somente dados do usuário logado
    def get_queryset(self):
        # O object_list é o nome padrão para armazenar uma lista de objetos de um ListView
        self.object_list = Animal.objects.filter(usuario=self.request.user)
        return self.object_list 


##################### Detalhar ######################

class AnimalDetalhes(DetailView):
    # Define a classe do objeto a ser detalhado
    model = Animal
    # Qual o template para essa tela
    template_name = "adocao/detalhe/animal.html"

    
    # Está comentado porque neste caso não faz sentido... #
    # Pegar somente se o animal for do usuário cadastrado
    '''
    def get_object(self, queryset=None):
        # Busca somente o Animal com a pk da URL que pertence ao usuário
        # Se o usuário tentar alguma pk diferente, vai dar página 404
        self.object = get_object_or_404(Animal, pk=self.kwargs['pk'], usuario=self.request.user,)
        # Retorna o objeto que será enviado ao template
        return self.object
    '''

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # Colocar mais coisas no context
        # Por exemplo: fazer um filtro em outra classe que utiliza o ID (pk)
        # do objeto que está sendo exibido, podemos fazer um filtro com ele...
        # context['itens'] = ItensVenda.objects.filter(venda=self.object)

        # self.object retorna o objeto da classe definida aqui no model = xxxx
        # self.kwargs['pk'] retorna a pk que está lá na URL

        return context
