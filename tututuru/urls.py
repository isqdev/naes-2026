from django.urls import path
from .views import (
    EquipeCreateView,
    EquipeDeleteView,
    EquipeDetailView,
    EquipeListView,
    EquipeUpdateView,
)

urlpatterns = [
    path("", EquipeListView.as_view(), name="equipe_list"),
    path("novo/", EquipeCreateView.as_view(), name="equipe_create"),
    path("<int:pk>/", EquipeDetailView.as_view(), name="equipe_detail"),
    path("<int:pk>/editar/", EquipeUpdateView.as_view(), name="equipe_update"),
    path("<int:pk>/excluir/", EquipeDeleteView.as_view(), name="equipe_delete"),
]
