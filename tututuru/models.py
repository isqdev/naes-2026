from django.db import models

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    pais_origem = models.CharField(max_length=80)
    ano_fundacao = models.PositiveIntegerField()
    motor = models.CharField(max_length=80)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

