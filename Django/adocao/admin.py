from django.contrib import admin

from .models import Animal, Cidade, Estado, Raca, Tipo

# Register your models here.
admin.site.register(Animal)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Raca)
admin.site.register(Tipo)
