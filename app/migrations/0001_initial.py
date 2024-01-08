# Generated by Django 5.0 on 2023-12-31 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="contact",
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
                ("name", models.CharField(max_length=30)),
                ("emailID", models.EmailField(max_length=30)),
                ("desc", models.TextField(max_length=50)),
                ("phone", models.IntegerField(max_length=10)),
            ],
        ),
    ]
