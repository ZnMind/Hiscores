# Generated by Django 4.2.11 on 2024-04-26 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player",
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
                ("username", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Woodcutting",
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
                ("level", models.IntegerField(default=1)),
                ("experience", models.IntegerField(default=0)),
                ("experience_last", models.IntegerField(default=0)),
                ("experience_next", models.IntegerField(default=75)),
                (
                    "player",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="woodcutting",
                        to="skills.player",
                    ),
                ),
            ],
        ),
    ]
