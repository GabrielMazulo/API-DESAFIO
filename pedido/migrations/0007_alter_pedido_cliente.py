# Generated by Django 5.1.3 on 2024-11-10 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_rename_pedido_cliente_escolha'),
        ('pedido', '0006_pedido_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos_cliente', to='cliente.cliente'),
        ),
    ]