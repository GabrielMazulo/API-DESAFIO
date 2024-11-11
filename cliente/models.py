from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100, null=True, blank=True)
    pedido_cliente = models.CharField(max_length=100, default="None")

    def __str__(self):
        return self.nome

