# Generated by Django 4.1.3 on 2022-11-11 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_clientes_options_alter_tipo_cliente_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email_cliente',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]