# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-28 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='userlogintime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]