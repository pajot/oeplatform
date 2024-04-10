# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-01 09:32
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("modelview", "0009_auto_20160301_1030")]

    operations = [
        migrations.AlterField(
            model_name="energyscenario",
            name="tools_models",
            field=models.ForeignKey(
                help_text="Which model(s) and other tools have been used?",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="modelview.Energymodel",
                verbose_name="Tools",
            ),
        )
    ]
