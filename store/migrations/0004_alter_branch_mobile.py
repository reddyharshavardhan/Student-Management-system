# Generated by Django 4.2 on 2023-05-06 18:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_alter_branch_mobile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="branch",
            name="mobile",
            field=models.PositiveIntegerField(
                default=3, validators=[django.core.validators.MaxValueValidator(100)]
            ),
            preserve_default=False,
        ),
    ]
