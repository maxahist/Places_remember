# Generated by Django 5.0.6 on 2024-05-18 14:06

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Remember",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        srid=4326, verbose_name="Локация"
                    ),
                ),
            ],
        ),
    ]
