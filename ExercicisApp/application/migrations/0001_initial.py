# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 10:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivell', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Exercici',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciat', models.CharField(max_length=500)),
                ('comentari_professor', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('icon', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Resposta_possible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.CharField(max_length=500)),
                ('correcta', models.BooleanField()),
                ('resposta_possible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Exercici')),
            ],
        ),
        migrations.CreateModel(
            name='Resposta_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.CharField(max_length=500)),
                ('resposta_User', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.Exercici')),
            ],
        ),
        migrations.CreateModel(
            name='Tipus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='perfil',
            name='resposta_User',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.Resposta_user'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='tipus',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.Tipus'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='usuari',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exercici',
            name='exercici',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Materia'),
        ),
        migrations.AddField(
            model_name='curs',
            name='materia',
            field=models.ManyToManyField(to='application.Materia'),
        ),
        migrations.AddField(
            model_name='curs',
            name='usuari',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Perfil'),
        ),
    ]
