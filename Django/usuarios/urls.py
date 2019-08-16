from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    # Aqui vão suas urls
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html',
        extra_context={
            'titulo': 'Autenticação', 
            'botao': 'Entrar',
            'classe': 'btn-primary'
            }
    ), name='login'),

    path('sair/', auth_views.LogoutView.as_view(), name="logout"),

    path('alterar-senha/', auth_views.PasswordChangeView.as_view(
        template_name='usuarios/form.html',
        extra_context={
            'titulo': 'Alterar senha atual',
            'botao': 'Alterar',
            'classe': 'btn-success'
            },
        success_url=reverse_lazy('index')
    ), name="alterar-senha"),



]
