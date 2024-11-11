# Generated by Django 5.1.3 on 2024-11-10 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_rename_pedido_cliente_escolha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='escolha',
        ),
        migrations.AddField(
            model_name='cliente',
            name='opcao_escolhida',
            field=models.CharField(default='', max_length=100),
        ),
    ]