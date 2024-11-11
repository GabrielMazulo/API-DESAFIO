# Generated by Django 5.1.3 on 2024-11-11 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_alter_cliente_pedido_cliente'),
        ('pedido', '0010_alter_pedido_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pedidos_cliente', to='cliente.cliente'),
        ),
    ]
