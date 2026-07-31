from django.urls import path
from .views import IndexView, ContatoView, SobreView
# Importar as views para gerenciamento de usuarios
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView
)
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("mudar-senha", PasswordChangeView.as_view(), name="alterar-senha")
]
