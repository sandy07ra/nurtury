# Generated by Django 4.2.7 on 2024-03-30 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("image", models.ImageField(null=True, upload_to="images")),
                ("status", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Subcategory",
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
                ("subcategory_name", models.CharField(max_length=200)),
                ("subcategory_image", models.ImageField(null=True, upload_to="images")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Nurture.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("product_image", models.ImageField(null=True, upload_to="images")),
                ("original_price", models.IntegerField()),
                ("selling_price", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("description", models.TextField(max_length=700)),
                ("season", models.TextField(max_length=600)),
                ("scientific_name", models.CharField(max_length=100)),
                ("family", models.CharField(max_length=100)),
                (
                    "subcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Nurture.subcategory",
                    ),
                ),
            ],
        ),
    ]
