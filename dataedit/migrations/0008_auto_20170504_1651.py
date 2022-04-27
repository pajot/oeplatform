# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 14:51
from __future__ import unicode_literals

import datetime

from django.db import migrations, models
import django.utils

class Migration(migrations.Migration):

    dependencies = [("dataedit", "0007_auto_20160825_1028")]

    operations = [
        migrations.RemoveField(model_name="tablerevision", name="revision"),
        migrations.AddField(
            model_name="tablerevision",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=1000),
        ),
    ]
