# Generated by Django 3.2.7 on 2023-02-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factsheet', '0004_auto_20230220_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factsheet',
            name='acronym',
            field=models.CharField(default="Factsheet's acronym", max_length=100),
        ),
    ]
