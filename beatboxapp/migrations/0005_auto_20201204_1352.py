# Generated by Django 3.0.8 on 2020-12-04 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatboxapp', '0004_auto_20201204_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='duracao',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='duracao'),
        ),
        migrations.AlterField(
            model_name='musica',
            name='artistas',
            field=models.CharField(default='', max_length=150, verbose_name='artistas'),
        ),
        migrations.AlterField(
            model_name='musica',
            name='tipo',
            field=models.CharField(default=' ', max_length=150, verbose_name='tipo'),
        ),
    ]
