from django.db import models

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    pais_origem = models.CharField(max_length=80)
    ano_fundacao = models.PositiveIntegerField()
    motor = models.CharField(max_length=80)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"

    def __str__(self):
        return self.nome


class Piloto(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT, related_name="pilotos")
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    numero_largada = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["nome"]
        verbose_name = "Piloto"
        verbose_name_plural = "Pilotos"

    def __str__(self):
        return self.nome


class Carro(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT, related_name="carros")
    piloto = models.OneToOneField(Piloto, on_delete=models.SET_NULL, null=True, blank=True, related_name="carro")
    modelo = models.CharField(max_length=80)
    ano = models.PositiveIntegerField()
    numero_carro = models.PositiveSmallIntegerField()
    chassi = models.CharField(max_length=80)

    class Meta:
        ordering = ["modelo", "numero_carro"]
        verbose_name = "Carro"
        verbose_name_plural = "Carros"

    def __str__(self):
        return f"{self.modelo} #{self.numero_carro}"


class Circuito(models.Model):
    nome = models.CharField(max_length=120)
    pais = models.CharField(max_length=60)
    cidade = models.CharField(max_length=80)
    extensao_km = models.DecimalField(max_digits=5, decimal_places=2)
    numero_curvas = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["nome"]
        verbose_name = "Circuito"
        verbose_name_plural = "Circuitos"

    def __str__(self):
        return self.nome


class Corrida(models.Model):
    circuito = models.ForeignKey(Circuito, on_delete=models.PROTECT, related_name="corridas")
    nome = models.CharField(max_length=120)
    data = models.DateField()
    temporada = models.PositiveIntegerField()
    total_voltas = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["-data", "nome"]
        verbose_name = "Corrida"
        verbose_name_plural = "Corridas"

    def __str__(self):
        return f"{self.nome} {self.temporada}"


class ResultadoCorrida(models.Model):
    corrida = models.ForeignKey(Corrida, on_delete=models.CASCADE, related_name="resultados")
    piloto = models.ForeignKey(Piloto, on_delete=models.PROTECT, related_name="resultados")
    carro = models.ForeignKey(Carro, on_delete=models.PROTECT, related_name="resultados")
    posicao_largada = models.PositiveSmallIntegerField()
    posicao_final = models.PositiveSmallIntegerField()
    voltas_completadas = models.PositiveSmallIntegerField()
    tempo_total = models.DurationField()
    melhor_volta = models.DurationField()
    pontos_obtidos = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=40)

    class Meta:
        ordering = ["corrida", "posicao_final"]
        verbose_name = "Resultado da Corrida"
        verbose_name_plural = "Resultados das Corridas"

    def __str__(self):
        return f"{self.corrida} - {self.piloto}"
