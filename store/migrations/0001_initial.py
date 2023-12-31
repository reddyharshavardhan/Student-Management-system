# Generated by Django 4.2 on 2023-05-06 17:32

from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Group",
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
                ("slug", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to=store.models.get_file_path
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Branch",
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
                ("Reg", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                (
                    "student_image",
                    models.ImageField(
                        blank=True, null=True, upload_to=store.models.get_file_path
                    ),
                ),
                ("gender", models.CharField(max_length=100)),
                ("dob", models.DateField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("address", models.TextField(max_length=500)),
                (
                    "status",
                    models.BooleanField(default=False, help_text="0-Fail, 1-Pass"),
                ),
                (
                    "Group",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="store.group"
                    ),
                ),
            ],
        ),
    ]
