# Generated by Django 3.0.4 on 2020-11-03 19:37

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dataedit", "0013_auto_20170810_1031"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="color",
            field=colorfield.fields.ColorField(default="#FF0000", max_length=18),
        ),
    ]
