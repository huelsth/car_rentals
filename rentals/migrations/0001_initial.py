# Generated by Django 5.0.2 on 2024-05-17 08:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarModel",
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
                ("name", models.CharField(max_length=100)),
                ("price_per_day", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "price_per_week",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("available", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Driver",
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
                ("name", models.CharField(max_length=100)),
                ("license_number", models.CharField(max_length=100)),
                ("id_card_number", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Extra",
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
                ("name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
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
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("Credit Card", "Credit Card"),
                            ("Debit Card", "Debit Card"),
                            ("Cash", "Cash"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "car_model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rentals.carmodel",
                    ),
                ),
                (
                    "driver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rentals.driver"
                    ),
                ),
                ("extras", models.ManyToManyField(to="rentals.extra")),
            ],
        ),
    ]
