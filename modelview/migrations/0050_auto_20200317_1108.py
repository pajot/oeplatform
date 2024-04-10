# Generated by Django 3.0.2 on 2020-03-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("modelview", "0049_auto_20200309_1635"),
    ]

    operations = [
        migrations.AlterField(
            model_name="energymodel",
            name="typical_computation_time",
            field=models.CharField(
                choices=[
                    ("less than a second", "less than a second"),
                    ("less than a minute", "less than a minute"),
                    ("less than an hour", "less than an hour"),
                    ("less than a day", "less than a day"),
                    ("more than a day", "more than a day"),
                ],
                max_length=30,
                null=True,
            ),
        ),
    ]
