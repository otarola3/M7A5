# Generated by Django 4.2.1 on 2023-05-31 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_m7', '0009_pedido_detalle_alter_pedido_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='detalle',
            field=models.CharField(default='', max_length=100),
        ),
    ]
