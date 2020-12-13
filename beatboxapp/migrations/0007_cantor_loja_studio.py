# Generated by Django 3.0.8 on 2020-12-04 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatboxapp', '0006_auto_20201204_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='cantor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=200, verbose_name='nome')),
                ('contacto', models.CharField(default='+258', max_length=15, verbose_name='contacto')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='email')),
                ('links', models.CharField(blank=True, default='', max_length=500, verbose_name='links')),
                ('data_de_nascimento', models.DateField(verbose_name='data_de_nascimento')),
                ('sobre', models.TextField(blank=True, default='A/O melhor artista de sempre', verbose_name='sobre')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data_de_criacao')),
                ('imagem', models.ImageField(blank=True, upload_to='', verbose_name='imagem')),
                ('denuncias', models.PositiveIntegerField(blank=True, default=0, verbose_name='denuncias')),
            ],
        ),
        migrations.CreateModel(
            name='loja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=200, verbose_name='nome')),
                ('pais', models.CharField(default='', max_length=200, verbose_name='pais')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data_de_criacao')),
                ('imagem', models.ImageField(blank=True, upload_to='', verbose_name='imagem')),
                ('sobre', models.TextField(blank=True, default='O melhor studio de sempre', verbose_name='sobre')),
                ('provincia', models.CharField(default='', max_length=200, verbose_name='provincia')),
                ('cidade', models.CharField(default='', max_length=200, verbose_name='cidade')),
                ('de', models.PositiveIntegerField(blank=True, default=0, verbose_name='de')),
                ('localizacao', models.CharField(default='', max_length=200, verbose_name='localizacao')),
                ('denuncias', models.PositiveIntegerField(blank=True, default=0, verbose_name='denuncias')),
            ],
        ),
        migrations.CreateModel(
            name='studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=200, verbose_name='nome')),
                ('pais', models.CharField(default='', max_length=200, verbose_name='pais')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data_de_criacao')),
                ('imagem', models.ImageField(blank=True, upload_to='', verbose_name='imagem')),
                ('sobre', models.TextField(blank=True, default='O melhor studio de sempre', verbose_name='sobre')),
                ('provincia', models.CharField(default='', max_length=200, verbose_name='provincia')),
                ('cidade', models.CharField(default='', max_length=200, verbose_name='cidade')),
                ('de', models.PositiveIntegerField(blank=True, default=0, verbose_name='de')),
                ('localizacao', models.CharField(default='', max_length=200, verbose_name='localizacao')),
                ('denuncias', models.PositiveIntegerField(blank=True, default=0, verbose_name='denuncias')),
            ],
        ),
    ]
