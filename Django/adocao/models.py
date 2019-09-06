from django.db import models

# Importar o modelo User
from django.contrib.auth.models import User

# Create your models here.


class Estado(models.Model):
    # nome_do_atributo = models.Tipo(configuração)
    sigla = models.CharField(max_length=2, unique=True)
    nome = models.CharField(max_length=50)

    # Como se fosse toString e self = this
    def __str__(self):
        return self.sigla + ' - ' + self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    descricao = models.TextField(
        blank=True, null=True, verbose_name="Descrição",
        help_text="Espaço para colocar qualquer informação."
    )

    def __str__(self):
        return self.nome + '/' + self.estado.sigla


class Tipo(models.Model):
    descricao = models.CharField(
        max_length=50, verbose_name="Descrição", help_text="Ex: gato, cachorro, pássarinho")

    def __str__(self):
        return "{}".format(self.descricao)


class Raca(models.Model):
    descricao = models.CharField(
        max_length=50, verbose_name="Descrição", help_text="Ex: vira-lata, beagle, pardal, persa")

    def __str__(self):
        return "{}".format(self.descricao)

    # Configurar algumas coisas dessa classe, como nome, plural, ordenação, etc
    # https://docs.djangoproject.com/en/2.2/ref/models/options/
    class Meta:
        verbose_name = "Raça"


class Animal(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    raca = models.ForeignKey(
        Raca, on_delete=models.PROTECT, verbose_name="Raça")
    descricao = models.CharField(
        max_length=250, verbose_name="Descrição", help_text="Ex: vira-lata, beagle, pardal, persa")
    nome = models.CharField(max_length=50, null=True, blank=True, help_text="O animal tem nome?")
    idade = models.DecimalField(max_digits=3, decimal_places=1, null=True,
                                help_text="Quantos anos, aproximadamente, o animal tem? Ex: 2,5")
    foto = models.URLField(help_text="Informe a URL de uma imagem para este animal. Ex: http://...")
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, help_text="Onde o animal está?")
    telefone = models.CharField(max_length=17)

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}/{}".format(self.nome, self.raca, self.tipo)
