# Generated by Django 3.0.8 on 2021-04-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatboxapp', '0025_auto_20210125_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='tam_audio',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='tam_audio'),
        ),
        migrations.AddField(
            model_name='musica',
            name='tam_video',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='tam_audio'),
        ),
    ]
