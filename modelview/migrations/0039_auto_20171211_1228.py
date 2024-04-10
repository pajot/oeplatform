# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-11 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("modelview", "0038_auto_20171130_1930")]

    operations = [
        migrations.AddField(
            model_name="basicfactsheet",
            name="methodical_focus_1",
            field=models.CharField(
                default="",
                help_text='1-3 Keyords descrybing the main methodical focus of the model e.g."open source", "sector coupling"',  # noqa
                max_length=50,
                verbose_name="Methodical Focus",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="basicfactsheet",
            name="methodical_focus_2",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="basicfactsheet",
            name="methodical_focus_3",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="energymodel",
            name="properties_missed",
            field=models.TextField(
                help_text="Which properties of your model have not been mentioned on this factsheet? Please note them.",  # noqa
                null=True,
                verbose_name="further properties",
            ),
        ),
    ]
