# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_thesis_thesis'),
    ]

    operations = [
        migrations.AddField(
            model_name='statustypes',
            name='description',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
