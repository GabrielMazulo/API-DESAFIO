# Generated by Django 5.1.3 on 2024-11-10 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_remove_cliente_escolha_cliente_opcao_escolhida'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='opcao_escolhida',
            new_name='pedido_cliente',
        ),
    ]
