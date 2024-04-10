# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-24 16:01
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("modelview", "0034_auto_20160426_1106")]

    operations = [
        migrations.RemoveField(model_name="energymodel", name="validation"),
        migrations.AddField(
            model_name="energymodel",
            name="validation_measurements",
            field=models.BooleanField(
                default=False, verbose_name="checked with measurements (measured data)"
            ),
        ),
        migrations.AddField(
            model_name="energymodel",
            name="validation_models",
            field=models.BooleanField(
                default=False, verbose_name="cross-checked with other models"
            ),
        ),
        migrations.AddField(
            model_name="energymodel",
            name="validation_others",
            field=models.BooleanField(default=False, verbose_name="others"),
        ),
        migrations.AddField(
            model_name="energymodel",
            name="validation_others_text",
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="basicfactsheet",
            name="modelling_software",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    help_text="What modelling software and which version is used?",
                    max_length=1000,
                ),
                default=list,
                size=None,
                verbose_name="Modelling software ",
            ),
        ),
        migrations.AlterField(
            model_name="basicfactsheet",
            name="source_of_funding",
            field=models.CharField(
                help_text="What is the main source of funding?",
                max_length=200,
                null=True,
                verbose_name="Source of funding",
            ),
        ),
        migrations.AlterField(
            model_name="energymodel",
            name="model_file_format",
            field=models.CharField(
                choices=[
                    (".exe", ".exe"),
                    (".gms", ".gms"),
                    (".py", ".py"),
                    (".xls", ".xls"),
                    ("Other", "Other"),
                ],
                default="other",
                help_text="In which format is the model saved?",
                max_length=5,
                null=True,
                verbose_name="Model file format",
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="energy_saving_amount",
            field=models.SmallIntegerField(
                help_text="development of energy savings or efficiency",
                null=True,
                verbose_name="Energy savings",
            ),
        ),
    ]
