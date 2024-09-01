# Generated by Django 4.2.14 on 2024-08-14 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0011_alter_futbol_a_ml_prob_alter_futbol_a_sb_prob_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='futbol',
            name='A_BB_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Best AVG A'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='A_MA_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Money AVG A'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='B_BB_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Best AVG B'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='B_MA_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Money AVG B'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='C_BB_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Best AVG C'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='C_MA_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Money AVG C'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='D_BB_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Best AVG D'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='D_MA_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Money AVG D'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='E_BB_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Best AVG E'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='E_MA_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Money AVG E'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='F_BB_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Best AVG F'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='F_MA_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Money AVG F'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='G_BB_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Best AVG G'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='G_MA_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Money AVG G'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='H_BB_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Best AVG H'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='H_MA_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Money AVG H'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='I_BB_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Best AVG I'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='I_MA_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Money AVG I'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='J_BB_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Best AVG J'),
        ),
        migrations.AddField(
            model_name='futbol',
            name='J_MA_prob',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Money AVG J'),
        ),
    ]
