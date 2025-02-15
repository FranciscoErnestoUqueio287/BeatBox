# Generated by Django 3.0.8 on 2020-12-05 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatboxapp', '0011_auto_20201205_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='cantor',
            name='confirmed_contacto',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cantor',
            name='confirmed_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cantor',
            name='pais',
            field=models.CharField(default='', max_length=200, verbose_name='pais'),
        ),
        migrations.AddField(
            model_name='loja',
            name='contacto',
            field=models.CharField(default='+258', max_length=15, verbose_name='contacto'),
        ),
        migrations.AddField(
            model_name='studio',
            name='contacto',
            field=models.CharField(default='+258', max_length=15, verbose_name='contacto'),
        ),
    ]
