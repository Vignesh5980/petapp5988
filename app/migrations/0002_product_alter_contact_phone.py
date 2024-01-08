# Generated by Django 5.0 on 2024-01-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="product",
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
                ("product_name", models.CharField(max_length=100)),
                ("category", models.CharField(default=" ", max_length=100)),
                ("sub_category", models.CharField(default=" ", max_length=100)),
                ("price", models.IntegerField(default=0)),
                ("desc", models.TextField(max_length=500)),
                ("image", models.ImageField(upload_to="images/images")),
            ],
        ),
        migrations.AlterField(
            model_name="contact",
            name="phone",
            field=models.IntegerField(),
        ),
    ]
