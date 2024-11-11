from django.db import models
from cliente.models import Cliente

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pedidos_cliente")
    status = models.CharField(max_length=100, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data_pedido = models.DateTimeField()

    def __str__(self):
        return f"Pedido {self.id} - {self.status}"

