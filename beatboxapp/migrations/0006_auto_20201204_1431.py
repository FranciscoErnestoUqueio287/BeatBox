# Generated by Django 3.0.8 on 2020-12-04 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatboxapp', '0005_auto_20201204_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='de',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='de'),
        ),
        migrations.AddField(
            model_name='musica',
            name='denuncias',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='denuncias'),
        ),
        migrations.AddField(
            model_name='musica',
            name='downloads',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='downloads'),
        ),
    ]
