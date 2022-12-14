# Generated by Django 4.1.3 on 2022-11-22 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dbsqlite", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="dbsqlite",
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
                ("name", models.CharField(default="", max_length=50)),
                ("age", models.CharField(default="", max_length=50)),
                ("password", models.CharField(default="", max_length=50)),
                ("email", models.CharField(default="", max_length=50)),
                ("father_name", models.CharField(default="", max_length=50)),
                ("our_image", models.ImageField(default="", upload_to="image")),
            ],
        ),
        migrations.DeleteModel(name="house",),
    ]
