# Generated by Django 3.0 on 2020-09-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modelview", "0055_auto_20200908_2126"),
    ]

    operations = [
        migrations.AlterField(
            model_name="energyframework",
            name="ap_Other",
            field=models.CharField(max_length=400, null=True, verbose_name="Other"),
        ),
    ]
