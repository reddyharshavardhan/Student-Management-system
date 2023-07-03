# Generated by Django 4.2 on 2023-05-06 18:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="branch",
            name="mobile",
            field=models.IntegerField(
                default=3,
                validators=[
                    django.core.validators.MaxValueValidator(9999999999),
                    django.core.validators.MinValueValidator(1000000000),
                ],
            ),
            preserve_default=False,
        ),
    ]
