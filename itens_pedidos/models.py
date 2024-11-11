from django.db import models


class Itens_pedidos(models.Model):
    nome_itens = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100, null=True, blank=True) 

    def __str__(self):
        return self.nome_itens
