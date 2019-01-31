# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-31 23:15
from __future__ import unicode_literals

from django.db import migrations, models

import localized_recurrence.models


class Migration(migrations.Migration):
    dependencies = [
        ('localized_recurrence', '0004_auto_20161108_2151'),
    ]
    operations = [
        migrations.AlterField(
            model_name='localizedrecurrence',
            name='next_scheduled',
            field=models.DateTimeField(default=localized_recurrence.models.default_scheduled),
        ),
        migrations.AlterField(
            model_name='localizedrecurrence',
            name='previous_scheduled',
            field=models.DateTimeField(default=localized_recurrence.models.default_scheduled),
        ),
    ]