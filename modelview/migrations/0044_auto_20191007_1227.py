# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-07 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("modelview", "0043_merge_20190425_1036"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="energyscenario",
            name="networks_electricity_gas_electricity",
        ),
        migrations.RemoveField(
            model_name="energyscenario",
            name="networks_electricity_gas_gas",
        ),
        migrations.AlterField(
            model_name="basicfactsheet",
            name="logo",
            field=models.ImageField(
                help_text="If a logo for the model exists load it up",
                null=True,
                upload_to="logos",
                verbose_name="Logo",
            ),
        ),
        migrations.AlterField(
            model_name="basicfactsheet",
            name="methodical_focus_1",
            field=models.CharField(
                help_text='1-3 Keyords describing the main methodical focus of the model e.g."open source", "sector coupling"',  # noqa
                max_length=50,
                verbose_name="Methodical Focus",
            ),
        ),
        migrations.AlterField(
            model_name="basicfactsheet",
            name="source_of_funding",
            field=models.CharField(
                help_text="What is the main source of funding for the development of the model?",  # noqa
                max_length=200,
                null=True,
                verbose_name="Source of funding",
            ),
        ),
    ]
