# Generated by Django 3.2.15 on 2022-10-05 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_transaccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='monto',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]