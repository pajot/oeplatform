# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-11 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("modelview", "0039_auto_20171211_1228")]

    operations = [
        migrations.AlterField(
            model_name="basicfactsheet",
            name="methodical_focus_2",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="basicfactsheet",
            name="methodical_focus_3",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
