# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-26 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIapp', '0002_auto_20170726_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='mapImage',
            field=models.CharField(max_length=1000),
        ),
    ]