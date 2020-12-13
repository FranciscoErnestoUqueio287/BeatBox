# Generated by Django 3.0.8 on 2020-12-04 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatboxapp', '0007_cantor_loja_studio'),
    ]

    operations = [
        migrations.AddField(
            model_name='cantor',
            name='gostos',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='gostos'),
        ),
        migrations.AddField(
            model_name='loja',
            name='gostos',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='gostos'),
        ),
        migrations.AddField(
            model_name='musica',
            name='gostos',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='gostos'),
        ),
        migrations.AddField(
            model_name='studio',
            name='gostos',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='gostos'),
        ),
    ]
