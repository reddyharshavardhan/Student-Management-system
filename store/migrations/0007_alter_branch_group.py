# Generated by Django 4.2 on 2023-05-06 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_alter_branch_mobile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="branch",
            name="Group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="store.group"
            ),
        ),
    ]
