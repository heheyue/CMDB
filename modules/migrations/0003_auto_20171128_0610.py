# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-28 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0002_auto_20171128_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='usertoken',
            field=models.CharField(max_length=32),
        ),
    ]