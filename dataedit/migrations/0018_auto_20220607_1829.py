# Generated by Django 3.2.13 on 2022-06-07 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataedit', '0017_alter_tablerevision_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schema',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='table',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
