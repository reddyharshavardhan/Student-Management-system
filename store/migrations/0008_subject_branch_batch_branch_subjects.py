# Generated by Django 4.2 on 2023-05-28 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0007_alter_branch_group"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subject",
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
                ("Code", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("credits", models.IntegerField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name="branch",
            name="Batch",
            field=models.IntegerField(default=3, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="branch",
            name="subjects",
            field=models.ManyToManyField(to="store.subject"),
        ),
    ]
