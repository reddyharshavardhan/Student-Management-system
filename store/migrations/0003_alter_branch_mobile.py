# Generated by Django 4.2 on 2023-05-06 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_branch_mobile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="branch",
            name="mobile",
            field=models.IntegerField(null=True),
        ),
    ]
