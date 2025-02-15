# Generated by Django 3.0.8 on 2020-12-05 08:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('beatboxapp', '0009_auto_20201204_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('byte', models.TextField()),
                ('filename', models.CharField(max_length=300)),
                ('mimetype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('byte', models.TextField()),
                ('filename', models.CharField(max_length=300)),
                ('mimetype', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='loja',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='musica',
            name='arquivo',
        ),
        migrations.AddField(
            model_name='loja',
            name='pr_nome',
            field=models.CharField(default='', max_length=200, verbose_name='pr_nome'),
        ),
        migrations.AddField(
            model_name='loja',
            name='ul_nome',
            field=models.CharField(default='', max_length=200, verbose_name='ul_nome'),
        ),
        migrations.AddField(
            model_name='musica',
            name='video',
            field=models.FileField(default=django.utils.timezone.now, upload_to='beatboxapp.video/byte/filename/mimetype', verbose_name='arquivo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cantor',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='beatboxapp.imagem/byte/filename/mimetype', verbose_name='imagem'),
        ),
        migrations.AlterField(
            model_name='loja',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='beatboxapp.imagem/byte/filename/mimetype', verbose_name='imagem'),
        ),
        migrations.AlterField(
            model_name='musica',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='beatboxapp.imagem/byte/filename/mimetype', verbose_name='imagem'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='beatboxapp.imagem/byte/filename/mimetype', verbose_name='imagem'),
        ),
    ]
