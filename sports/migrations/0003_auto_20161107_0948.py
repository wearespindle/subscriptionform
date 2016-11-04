# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_auto_20161104_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='sportdetail',
            name='detail',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sports.Detail'),
        ),
    ]