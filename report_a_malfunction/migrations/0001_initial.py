# Generated by Django 4.2.1 on 2023-05-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Malfunction",
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
                ("name", models.CharField(max_length=200)),
                ("location", models.CharField(max_length=300)),
                ("explanation", models.CharField(max_length=500)),
            ],
        ),
    ]