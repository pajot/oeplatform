# Generated by Django 3.0 on 2021-03-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0006_auto_20210311_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='license',
            field=models.CharField(choices=[('none', 'No'), ('cc0', 'CC0'), ('agpl', 'AGPL')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='category',
            field=models.CharField(blank=True, choices=[('publication', 'Publication'), ('io', 'I/O'), ('intro', 'OEP Introduction'), ('ontology', 'Ontology'), ('other', 'Other')], max_length=15),
        ),
    ]
