# Generated by Django 5.1.3 on 2024-11-11 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens_pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itens_pedidos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
