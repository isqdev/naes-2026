from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Equipe


class EquipeListView(ListView):
	model = Equipe
	template_name = "tututuru/equipe_list.html"
	context_object_name = "equipes"


class EquipeDetailView(DetailView):
	model = Equipe
	template_name = "tututuru/equipe_detail.html"
	context_object_name = "equipe"


class EquipeCreateView(CreateView):
	model = Equipe
	template_name = "tututuru/equipe_form.html"
	fields = ["nome", "pais_origem", "ano_fundacao", "motor"]
	success_url = reverse_lazy("equipe_list")


class EquipeUpdateView(UpdateView):
	model = Equipe
	template_name = "tututuru/equipe_form.html"
	fields = ["nome", "pais_origem", "ano_fundacao", "motor"]
	success_url = reverse_lazy("equipe_list")


class EquipeDeleteView(DeleteView):
	model = Equipe
	template_name = "tututuru/equipe_confirm_delete.html"
	success_url = reverse_lazy("equipe_list")
