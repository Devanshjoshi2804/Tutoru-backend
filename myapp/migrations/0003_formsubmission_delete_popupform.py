# Generated by Django 5.0.7 on 2024-07-14 09:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_popupform_delete_formdata"),
    ]

    operations = [
        migrations.CreateModel(
            name="FormSubmission",
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
                ("phone", models.CharField(max_length=15)),
                ("grade", models.CharField(blank=True, max_length=2, null=True)),
                ("subjects", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="PopupForm",
        ),
    ]
