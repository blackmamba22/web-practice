# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-11 21:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20160311_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]