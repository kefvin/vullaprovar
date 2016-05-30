# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_exercici_tema'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercici',
            old_name='exercici',
            new_name='materia',
        ),
        migrations.RenameField(
            model_name='resposta_possible',
            old_name='resposta_possible',
            new_name='exercici',
        ),
        migrations.RenameField(
            model_name='resposta_user',
            old_name='resposta_User',
            new_name='exercici',
        ),
        migrations.RemoveField(
            model_name='curs',
            name='usuari',
        ),
        migrations.AddField(
            model_name='perfil',
            name='curs',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='application.Curs'),
            preserve_default=False,
        ),
    ]