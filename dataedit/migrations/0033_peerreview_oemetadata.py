# Generated by Django 3.2.22 on 2024-03-20 14:10

from django.db import migrations, models


# def update_oemetadata_to_empty_dict(apps, schema_editor):
#     PeerReview = apps.get_model("dataedit", "PeerReview")
#     # Filter for peer reviews where `oemetadata` is None (aka null)
#     # and update them to have an empty dictionary instead.
#     PeerReview.objects.filter(oemetadata__isnull=True).update(oemetadata=dict())


def populate_oemetadata(apps, schema_editor):
    PeerReview = apps.get_model("dataedit", "PeerReview")
    TableModel = apps.get_model(
        "dataedit", "Table"
    ) 
    for review in PeerReview.objects.all():
        if not review.oemetadata or review.oemetadata == {}:
            # Logic to find a matching value from TableModel.
            table = TableModel.objects.filter(
                schema=review.schema, name=review.table
            ).first()
            if table:
                review.oemetadata = table.oemetadata
                review.save()


class Migration(migrations.Migration):

    dependencies = [
        ("dataedit", "0032_alter_table_is_publish"),
    ]

    operations = [
        migrations.AddField(
            model_name="peerreview",
            name="oemetadata",
            field=models.JSONField(default=dict),
        ),
        migrations.RunPython(populate_oemetadata),
    ]
