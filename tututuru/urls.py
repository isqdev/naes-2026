from django.urls import path

from .views import (
    CarroCreateView,
    CarroDeleteView,
    CarroDetailView,
    CarroListView,
    CarroUpdateView,
    CircuitoCreateView,
    CircuitoDeleteView,
    CircuitoDetailView,
    CircuitoListView,
    CircuitoUpdateView,
    CorridaCreateView,
    CorridaDeleteView,
    CorridaDetailView,
    CorridaListView,
    CorridaUpdateView,
    EquipeCreateView,
    EquipeDeleteView,
    EquipeDetailView,
    EquipeListView,
    EquipeUpdateView,
    PilotoCreateView,
    PilotoDeleteView,
    PilotoDetailView,
    PilotoListView,
    PilotoUpdateView,
    ResultadoCorridaCreateView,
    ResultadoCorridaDeleteView,
    ResultadoCorridaDetailView,
    ResultadoCorridaListView,
    ResultadoCorridaUpdateView,
)

app_name = "tututuru"

urlpatterns = [
    path("equipes/", EquipeListView.as_view(), name="equipe-lista"),
    path("equipes/novo/", EquipeCreateView.as_view(), name="equipe-criar"),
    path("equipes/<int:pk>/", EquipeDetailView.as_view(), name="equipe-detalhe"),
    path("equipes/<int:pk>/editar/", EquipeUpdateView.as_view(), name="equipe-editar"),
    path("equipes/<int:pk>/excluir/", EquipeDeleteView.as_view(), name="equipe-excluir"),

    path("pilotos/", PilotoListView.as_view(), name="piloto-lista"),
    path("pilotos/novo/", PilotoCreateView.as_view(), name="piloto-criar"),
    path("pilotos/<int:pk>/", PilotoDetailView.as_view(), name="piloto-detalhe"),
    path("pilotos/<int:pk>/editar/", PilotoUpdateView.as_view(), name="piloto-editar"),
    path("pilotos/<int:pk>/excluir/", PilotoDeleteView.as_view(), name="piloto-excluir"),

    path("carros/", CarroListView.as_view(), name="carro-lista"),
    path("carros/novo/", CarroCreateView.as_view(), name="carro-criar"),
    path("carros/<int:pk>/", CarroDetailView.as_view(), name="carro-detalhe"),
    path("carros/<int:pk>/editar/", CarroUpdateView.as_view(), name="carro-editar"),
    path("carros/<int:pk>/excluir/", CarroDeleteView.as_view(), name="carro-excluir"),

    path("circuitos/", CircuitoListView.as_view(), name="circuito-lista"),
    path("circuitos/novo/", CircuitoCreateView.as_view(), name="circuito-criar"),
    path("circuitos/<int:pk>/", CircuitoDetailView.as_view(), name="circuito-detalhe"),
    path("circuitos/<int:pk>/editar/", CircuitoUpdateView.as_view(), name="circuito-editar"),
    path("circuitos/<int:pk>/excluir/", CircuitoDeleteView.as_view(), name="circuito-excluir"),

    path("corridas/", CorridaListView.as_view(), name="corrida-lista"),
    path("corridas/novo/", CorridaCreateView.as_view(), name="corrida-criar"),
    path("corridas/<int:pk>/", CorridaDetailView.as_view(), name="corrida-detalhe"),
    path("corridas/<int:pk>/editar/", CorridaUpdateView.as_view(), name="corrida-editar"),
    path("corridas/<int:pk>/excluir/", CorridaDeleteView.as_view(), name="corrida-excluir"),

    path("resultados/", ResultadoCorridaListView.as_view(), name="resultado-lista"),
    path("resultados/novo/", ResultadoCorridaCreateView.as_view(), name="resultado-criar"),
    path("resultados/<int:pk>/", ResultadoCorridaDetailView.as_view(), name="resultado-detalhe"),
    path("resultados/<int:pk>/editar/", ResultadoCorridaUpdateView.as_view(), name="resultado-editar"),
    path("resultados/<int:pk>/excluir/", ResultadoCorridaDeleteView.as_view(), name="resultado-excluir"),
]
