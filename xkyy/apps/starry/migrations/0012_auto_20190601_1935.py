# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-06-01 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('starry', '0011_auto_20190601_1858'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='readnum',
            options={'verbose_name': '阅读数', 'verbose_name_plural': '阅读数'},
        ),
        migrations.AlterField(
            model_name='readnum',
            name='article',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='starry.Article'),
        ),
    ]
