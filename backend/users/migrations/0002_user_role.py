# Generated by Django 4.1.7 on 2023-04-22 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.IntegerField(
                choices=[
                    (1, "Tenant"),
                    (2, "Landlord"),
                    (3, "General Manager"),
                    (4, "Listing Manager"),
                    (5, "Financial Manager"),
                ],
                default=1,
            ),
        ),
    ]
