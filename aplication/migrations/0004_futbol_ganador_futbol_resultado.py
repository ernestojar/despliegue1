# Generated by Django 4.2.14 on 2024-08-03 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0003_alter_baseball_a_bb_alter_baseball_a_ma_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='futbol',
            name='ganador',
            field=models.CharField(blank=True, default='Empate', max_length=100, null=True, verbose_name='Ganador'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='resultado',
            field=models.CharField(blank=True, default='0-0', max_length=100, null=True, verbose_name='Resultado'),
        ),
    ]
