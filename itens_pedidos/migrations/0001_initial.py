# Generated by Django 5.1.3 on 2024-11-10 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Itens_pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_itens', models.CharField(max_length=100)),
                ('descricao', models.CharField(blank=True, max_length=100, null=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
