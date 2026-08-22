from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import (
	CarroForm,
	CircuitoForm,
	CorridaForm,
	EquipeForm,
	PilotoForm,
	ResultadoCorridaForm,
)
from .models import Carro, Circuito, Corrida, Equipe, Piloto, ResultadoCorrida


class UsuarioQuerysetMixin(LoginRequiredMixin):
	"""Restringe leitura, alteração e exclusão aos registros do usuário atual."""

	def get_queryset(self):
		return super().get_queryset().filter(usuario=self.request.user)


class UsuarioCreateMixin(LoginRequiredMixin):
	"""Associa automaticamente o usuário autenticado ao novo registro."""

	def form_valid(self, form):
		form.instance.usuario = self.request.user
		return super().form_valid(form)


class GerenciadorRequiredMixin(GroupRequiredMixin):
	"""Exclusões são restritas ao grupo Gerenciadores."""

	group_required = "Gerenciadores"
	raise_exception = True


class EquipeListView(UsuarioQuerysetMixin, ListView):
	model = Equipe
	template_name = "tututuru/equipe_list.html"
	context_object_name = "equipes"
	paginate_by = 10
	extra_context = {"titulo": "Equipes"}


class EquipeDetailView(UsuarioQuerysetMixin, DetailView):
	model = Equipe
	template_name = "tututuru/equipe_detail.html"
	context_object_name = "equipe"

	def get_queryset(self):
		return super().get_queryset().prefetch_related("carros", "pilotos")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["carros"] = self.object.carros.all()
		context["pilotos"] = self.object.pilotos.all()
		return context


class EquipeCreateView(UsuarioCreateMixin, CreateView):
	model = Equipe
	template_name = "tututuru/equipe_form.html"
	form_class = EquipeForm
	success_url = reverse_lazy("tututuru:equipe-lista")
	extra_context = {"titulo": "Adicionar Equipe"}


class EquipeUpdateView(UsuarioQuerysetMixin, UpdateView):
	model = Equipe
	template_name = "tututuru/equipe_form.html"
	form_class = EquipeForm
	success_url = reverse_lazy("tututuru:equipe-lista")
	extra_context = {"titulo": "Editar Equipe"}


class EquipeDeleteView(GerenciadorRequiredMixin, UsuarioQuerysetMixin, DeleteView):
	model = Equipe
	template_name = "tututuru/equipe_confirm_delete.html"
	success_url = reverse_lazy("tututuru:equipe-lista")


class PilotoListView(UsuarioQuerysetMixin, ListView):
	model = Piloto
	template_name = "tututuru/piloto_list.html"
	context_object_name = "pilotos"
	paginate_by = 10
	extra_context = {"titulo": "Pilotos"}

	def get_queryset(self):
		return super().get_queryset().select_related("equipe")


class PilotoDetailView(UsuarioQuerysetMixin, DetailView):
	model = Piloto
	template_name = "tututuru/piloto_detail.html"
	context_object_name = "piloto"

	def get_queryset(self):
		return super().get_queryset().select_related("equipe").select_related("carro")


class PilotoCreateView(UsuarioCreateMixin, CreateView):
	model = Piloto
	template_name = "tututuru/piloto_form.html"
	form_class = PilotoForm
	success_url = reverse_lazy("tututuru:piloto-lista")
	extra_context = {"titulo": "Adicionar Piloto"}


class PilotoUpdateView(UsuarioQuerysetMixin, UpdateView):
	model = Piloto
	template_name = "tututuru/piloto_form.html"
	form_class = PilotoForm
	success_url = reverse_lazy("tututuru:piloto-lista")
	extra_context = {"titulo": "Editar Piloto"}


class PilotoDeleteView(GerenciadorRequiredMixin, UsuarioQuerysetMixin, DeleteView):
	model = Piloto
	template_name = "tututuru/piloto_confirm_delete.html"
	success_url = reverse_lazy("tututuru:piloto-lista")


class CarroListView(UsuarioQuerysetMixin, ListView):
	model = Carro
	template_name = "tututuru/carro_list.html"
	context_object_name = "carros"
	paginate_by = 10
	extra_context = {"titulo": "Carros"}

	def get_queryset(self):
		return super().get_queryset().select_related("equipe", "piloto")


class CarroDetailView(UsuarioQuerysetMixin, DetailView):
	model = Carro
	template_name = "tututuru/carro_detail.html"
	context_object_name = "carro"

	def get_queryset(self):
		return super().get_queryset().select_related("equipe", "piloto")


class CarroCreateView(UsuarioCreateMixin, CreateView):
	model = Carro
	template_name = "tututuru/carro_form.html"
	form_class = CarroForm
	success_url = reverse_lazy("tututuru:carro-lista")
	extra_context = {"titulo": "Adicionar Carro"}


class CarroUpdateView(UsuarioQuerysetMixin, UpdateView):
	model = Carro
	template_name = "tututuru/carro_form.html"
	form_class = CarroForm
	success_url = reverse_lazy("tututuru:carro-lista")
	extra_context = {"titulo": "Editar Carro"}


class CarroDeleteView(GerenciadorRequiredMixin, UsuarioQuerysetMixin, DeleteView):
	model = Carro
	template_name = "tututuru/carro_confirm_delete.html"
	success_url = reverse_lazy("tututuru:carro-lista")


class CircuitoListView(UsuarioQuerysetMixin, ListView):
	model = Circuito
	template_name = "tututuru/circuito_list.html"
	context_object_name = "circuitos"
	paginate_by = 10
	extra_context = {"titulo": "Circuitos"}


class CircuitoDetailView(UsuarioQuerysetMixin, DetailView):
	model = Circuito
	template_name = "tututuru/circuito_detail.html"
	context_object_name = "circuito"

	def get_queryset(self):
		return super().get_queryset().prefetch_related("corridas")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["corridas"] = self.object.corridas.all()
		return context


class CircuitoCreateView(UsuarioCreateMixin, CreateView):
	model = Circuito
	template_name = "tututuru/circuito_form.html"
	form_class = CircuitoForm
	success_url = reverse_lazy("tututuru:circuito-lista")
	extra_context = {"titulo": "Adicionar Circuito"}


class CircuitoUpdateView(UsuarioQuerysetMixin, UpdateView):
	model = Circuito
	template_name = "tututuru/circuito_form.html"
	form_class = CircuitoForm
	success_url = reverse_lazy("tututuru:circuito-lista")
	extra_context = {"titulo": "Editar Circuito"}


class CircuitoDeleteView(GerenciadorRequiredMixin, UsuarioQuerysetMixin, DeleteView):
	model = Circuito
	template_name = "tututuru/circuito_confirm_delete.html"
	success_url = reverse_lazy("tututuru:circuito-lista")


class CorridaListView(UsuarioQuerysetMixin, ListView):
	model = Corrida
	template_name = "tututuru/corrida_list.html"
	context_object_name = "corridas"
	paginate_by = 10
	extra_context = {"titulo": "Corridas"}

	def get_queryset(self):
		return super().get_queryset().select_related("circuito")


class CorridaDetailView(UsuarioQuerysetMixin, DetailView):
	model = Corrida
	template_name = "tututuru/corrida_detail.html"
	context_object_name = "corrida"

	def get_queryset(self):
		return (
			super()
			.get_queryset()
			.select_related("circuito")
			.prefetch_related("resultados__piloto", "resultados__carro")
		)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["resultados"] = self.object.resultados.select_related("piloto", "carro")
		return context


class CorridaCreateView(UsuarioCreateMixin, CreateView):
	model = Corrida
	template_name = "tututuru/corrida_form.html"
	form_class = CorridaForm
	success_url = reverse_lazy("tututuru:corrida-lista")
	extra_context = {"titulo": "Adicionar Corrida"}


class CorridaUpdateView(UsuarioQuerysetMixin, UpdateView):
	model = Corrida
	template_name = "tututuru/corrida_form.html"
	form_class = CorridaForm
	success_url = reverse_lazy("tututuru:corrida-lista")
	extra_context = {"titulo": "Editar Corrida"}


class CorridaDeleteView(GerenciadorRequiredMixin, UsuarioQuerysetMixin, DeleteView):
	model = Corrida
	template_name = "tututuru/corrida_confirm_delete.html"
	success_url = reverse_lazy("tututuru:corrida-lista")


class ResultadoCorridaListView(UsuarioQuerysetMixin, ListView):
	model = ResultadoCorrida
	template_name = "tututuru/resultado_list.html"
	context_object_name = "resultados"
	paginate_by = 10
	extra_context = {"titulo": "Resultados"}

	def get_queryset(self):
		return super().get_queryset().select_related("corrida", "piloto", "carro")


class ResultadoCorridaDetailView(UsuarioQuerysetMixin, DetailView):
	model = ResultadoCorrida
	template_name = "tututuru/resultado_detail.html"
	context_object_name = "resultado"

	def get_queryset(self):
		return super().get_queryset().select_related("corrida", "piloto", "carro")


class ResultadoCorridaCreateView(UsuarioCreateMixin, CreateView):
	model = ResultadoCorrida
	template_name = "tututuru/resultado_form.html"
	form_class = ResultadoCorridaForm
	success_url = reverse_lazy("tututuru:resultado-lista")
	extra_context = {"titulo": "Adicionar Resultado"}


class ResultadoCorridaUpdateView(UsuarioQuerysetMixin, UpdateView):
	model = ResultadoCorrida
	template_name = "tututuru/resultado_form.html"
	form_class = ResultadoCorridaForm
	success_url = reverse_lazy("tututuru:resultado-lista")
	extra_context = {"titulo": "Editar Resultado"}


class ResultadoCorridaDeleteView(GerenciadorRequiredMixin, UsuarioQuerysetMixin, DeleteView):
	model = ResultadoCorrida
	template_name = "tututuru/resultado_confirm_delete.html"
	success_url = reverse_lazy("tututuru:resultado-lista")
