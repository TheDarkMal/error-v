# Generated by Django 2.1 on 2019-08-29 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0004_auto_20190815_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleprestamo',
            name='fechadedevolucion',
            field=models.DateField(null=True, verbose_name='Fecha de devolucion'),
        ),
    ]
