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


class EquipeListView(ListView):
	model = Equipe
	template_name = "tututuru/equipe_list.html"
	context_object_name = "equipes"
	paginate_by = 10
	extra_context = {"titulo": "Equipes"}


class EquipeDetailView(DetailView):
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


class EquipeCreateView(CreateView):
	model = Equipe
	template_name = "tututuru/equipe_form.html"
	form_class = EquipeForm
	success_url = reverse_lazy("tututuru:equipe-lista")
	extra_context = {"titulo": "Adicionar Equipe"}


class EquipeUpdateView(UpdateView):
	model = Equipe
	template_name = "tututuru/equipe_form.html"
	form_class = EquipeForm
	success_url = reverse_lazy("tututuru:equipe-lista")
	extra_context = {"titulo": "Editar Equipe"}


class EquipeDeleteView(DeleteView):
	model = Equipe
	template_name = "tututuru/equipe_confirm_delete.html"
	success_url = reverse_lazy("tututuru:equipe-lista")


class PilotoListView(ListView):
	model = Piloto
	template_name = "tututuru/piloto_list.html"
	context_object_name = "pilotos"
	paginate_by = 10
	extra_context = {"titulo": "Pilotos"}

	def get_queryset(self):
		return super().get_queryset().select_related("equipe")


class PilotoDetailView(DetailView):
	model = Piloto
	template_name = "tututuru/piloto_detail.html"
	context_object_name = "piloto"

	def get_queryset(self):
		return super().get_queryset().select_related("equipe").select_related("carro")


class PilotoCreateView(CreateView):
	model = Piloto
	template_name = "tututuru/piloto_form.html"
	form_class = PilotoForm
	success_url = reverse_lazy("tututuru:piloto-lista")
	extra_context = {"titulo": "Adicionar Piloto"}


class PilotoUpdateView(UpdateView):
	model = Piloto
	template_name = "tututuru/piloto_form.html"
	form_class = PilotoForm
	success_url = reverse_lazy("tututuru:piloto-lista")
	extra_context = {"titulo": "Editar Piloto"}


class PilotoDeleteView(DeleteView):
	model = Piloto
	template_name = "tututuru/piloto_confirm_delete.html"
	success_url = reverse_lazy("tututuru:piloto-lista")


class CarroListView(ListView):
	model = Carro
	template_name = "tututuru/carro_list.html"
	context_object_name = "carros"
	paginate_by = 10
	extra_context = {"titulo": "Carros"}

	def get_queryset(self):
		return super().get_queryset().select_related("equipe", "piloto")


class CarroDetailView(DetailView):
	model = Carro
	template_name = "tututuru/carro_detail.html"
	context_object_name = "carro"

	def get_queryset(self):
		return super().get_queryset().select_related("equipe", "piloto")


class CarroCreateView(CreateView):
	model = Carro
	template_name = "tututuru/carro_form.html"
	form_class = CarroForm
	success_url = reverse_lazy("tututuru:carro-lista")
	extra_context = {"titulo": "Adicionar Carro"}


class CarroUpdateView(UpdateView):
	model = Carro
	template_name = "tututuru/carro_form.html"
	form_class = CarroForm
	success_url = reverse_lazy("tututuru:carro-lista")
	extra_context = {"titulo": "Editar Carro"}


class CarroDeleteView(DeleteView):
	model = Carro
	template_name = "tututuru/carro_confirm_delete.html"
	success_url = reverse_lazy("tututuru:carro-lista")


class CircuitoListView(ListView):
	model = Circuito
	template_name = "tututuru/circuito_list.html"
	context_object_name = "circuitos"
	paginate_by = 10
	extra_context = {"titulo": "Circuitos"}


class CircuitoDetailView(DetailView):
	model = Circuito
	template_name = "tututuru/circuito_detail.html"
	context_object_name = "circuito"

	def get_queryset(self):
		return super().get_queryset().prefetch_related("corridas")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["corridas"] = self.object.corridas.all()
		return context


class CircuitoCreateView(CreateView):
	model = Circuito
	template_name = "tututuru/circuito_form.html"
	form_class = CircuitoForm
	success_url = reverse_lazy("tututuru:circuito-lista")
	extra_context = {"titulo": "Adicionar Circuito"}


class CircuitoUpdateView(UpdateView):
	model = Circuito
	template_name = "tututuru/circuito_form.html"
	form_class = CircuitoForm
	success_url = reverse_lazy("tututuru:circuito-lista")
	extra_context = {"titulo": "Editar Circuito"}


class CircuitoDeleteView(DeleteView):
	model = Circuito
	template_name = "tututuru/circuito_confirm_delete.html"
	success_url = reverse_lazy("tututuru:circuito-lista")


class CorridaListView(ListView):
	model = Corrida
	template_name = "tututuru/corrida_list.html"
	context_object_name = "corridas"
	paginate_by = 10
	extra_context = {"titulo": "Corridas"}

	def get_queryset(self):
		return super().get_queryset().select_related("circuito")


class CorridaDetailView(DetailView):
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


class CorridaCreateView(CreateView):
	model = Corrida
	template_name = "tututuru/corrida_form.html"
	form_class = CorridaForm
	success_url = reverse_lazy("tututuru:corrida-lista")
	extra_context = {"titulo": "Adicionar Corrida"}


class CorridaUpdateView(UpdateView):
	model = Corrida
	template_name = "tututuru/corrida_form.html"
	form_class = CorridaForm
	success_url = reverse_lazy("tututuru:corrida-lista")
	extra_context = {"titulo": "Editar Corrida"}


class CorridaDeleteView(DeleteView):
	model = Corrida
	template_name = "tututuru/corrida_confirm_delete.html"
	success_url = reverse_lazy("tututuru:corrida-lista")


class ResultadoCorridaListView(ListView):
	model = ResultadoCorrida
	template_name = "tututuru/resultado_list.html"
	context_object_name = "resultados"
	paginate_by = 10
	extra_context = {"titulo": "Resultados"}

	def get_queryset(self):
		return super().get_queryset().select_related("corrida", "piloto", "carro")


class ResultadoCorridaDetailView(DetailView):
	model = ResultadoCorrida
	template_name = "tututuru/resultado_detail.html"
	context_object_name = "resultado"

	def get_queryset(self):
		return super().get_queryset().select_related("corrida", "piloto", "carro")


class ResultadoCorridaCreateView(CreateView):
	model = ResultadoCorrida
	template_name = "tututuru/resultado_form.html"
	form_class = ResultadoCorridaForm
	success_url = reverse_lazy("tututuru:resultado-lista")
	extra_context = {"titulo": "Adicionar Resultado"}


class ResultadoCorridaUpdateView(UpdateView):
	model = ResultadoCorrida
	template_name = "tututuru/resultado_form.html"
	form_class = ResultadoCorridaForm
	success_url = reverse_lazy("tututuru:resultado-lista")
	extra_context = {"titulo": "Editar Resultado"}


class ResultadoCorridaDeleteView(DeleteView):
	model = ResultadoCorrida
	template_name = "tututuru/resultado_confirm_delete.html"
	success_url = reverse_lazy("tututuru:resultado-lista")
