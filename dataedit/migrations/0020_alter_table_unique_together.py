# Generated by Django 3.2.18 on 2023-05-09 17:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dataedit", "0019_table_oemetadata"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="table",
            unique_together={("name",)},
        ),
    ]
