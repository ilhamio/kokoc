# Generated by Django 4.2.5 on 2023-09-30 16:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("competitions", "0003_teamcompetition_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PersonalCompetition",
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
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название турнира"),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("description", models.TextField(verbose_name="Описание турнира")),
                (
                    "participants",
                    models.ManyToManyField(
                        related_name="personal_competitions",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Участники",
                    ),
                ),
            ],
        ),
    ]
