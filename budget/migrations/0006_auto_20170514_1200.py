# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-14 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_auto_20170514_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='nom',
        ),
        migrations.AlterField(
            model_name='budget',
            name='nom_de_la_dépense',
            field=models.CharField(max_length=255),
        ),
    ]
