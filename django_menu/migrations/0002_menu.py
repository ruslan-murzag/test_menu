# Generated by Django 4.1.7 on 2023-03-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_menu", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("name", models.CharField(max_length=50)),
                ("items", models.ManyToManyField(to="django_menu.menuitem")),
            ],
        ),
    ]