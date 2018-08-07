# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-07 12:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='rate',
            new_name='rate_per_hour',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='rate_currency',
            new_name='rate_per_hour_currency',
        ),
        migrations.AlterField(
            model_name='service',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
