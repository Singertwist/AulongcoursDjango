# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-14 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_auto_20170514_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='categorie_depenses',
            field=models.CharField(choices=[('TRANSPORT', 'Transport'), ('HEBERGEMENTS', 'Hébergements'), ('RESTAURATION', 'Restauration'), ('VISITES', 'Visites'), ('AUTRES', 'Autres')], max_length=2),
        ),
    ]
