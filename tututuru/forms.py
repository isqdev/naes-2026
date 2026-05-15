from django import forms
from django.utils import timezone
from crispy_forms.helper import FormHelper

from .models import Carro, Circuito, Corrida, Equipe, Piloto, ResultadoCorrida


class BaseCrispyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class EquipeForm(BaseCrispyForm):
    class Meta:
        model = Equipe
        fields = ["nome", "pais_origem", "ano_fundacao", "motor"]

    def clean_ano_fundacao(self):
        ano = self.cleaned_data["ano_fundacao"]
        ano_atual = timezone.now().year
        if ano > ano_atual:
            raise forms.ValidationError("O ano de fundacao nao pode ser no futuro.")
        return ano


class PilotoForm(BaseCrispyForm):
    class Meta:
        model = Piloto
        fields = ["equipe", "nome", "nacionalidade", "data_nascimento", "numero_largada"]

    def clean_data_nascimento(self):
        data = self.cleaned_data["data_nascimento"]
        if data > timezone.now().date():
            raise forms.ValidationError("A data de nascimento nao pode ser no futuro.")
        return data


class CarroForm(BaseCrispyForm):
    class Meta:
        model = Carro
        fields = ["equipe", "piloto", "modelo", "ano", "numero_carro", "chassi"]

    def clean_ano(self):
        ano = self.cleaned_data["ano"]
        ano_atual = timezone.now().year
        if ano > ano_atual:
            raise forms.ValidationError("O ano do carro nao pode ser no futuro.")
        return ano


class CircuitoForm(BaseCrispyForm):
    class Meta:
        model = Circuito
        fields = ["nome", "pais", "cidade", "extensao_km", "numero_curvas"]

    def clean_extensao_km(self):
        extensao = self.cleaned_data["extensao_km"]
        if extensao <= 0:
            raise forms.ValidationError("A extensao precisa ser maior que zero.")
        return extensao


class CorridaForm(BaseCrispyForm):
    class Meta:
        model = Corrida
        fields = ["circuito", "nome", "data", "temporada", "total_voltas"]

    def clean_data(self):
        data = self.cleaned_data["data"]
        if data > timezone.now().date():
            raise forms.ValidationError("A data da corrida nao pode ser no futuro.")
        return data


class ResultadoCorridaForm(BaseCrispyForm):
    class Meta:
        model = ResultadoCorrida
        fields = [
            "corrida",
            "piloto",
            "carro",
            "posicao_largada",
            "posicao_final",
            "voltas_completadas",
            "tempo_total",
            "melhor_volta",
            "pontos_obtidos",
            "status",
        ]

    def clean_posicao_final(self):
        posicao = self.cleaned_data["posicao_final"]
        if posicao <= 0:
            raise forms.ValidationError("A posicao final deve ser positiva.")
        return posicao

