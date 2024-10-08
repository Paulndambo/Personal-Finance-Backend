# Generated by Django 5.1.1 on 2024-10-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loans", "0002_loan_date_due"),
    ]

    operations = [
        migrations.AddField(
            model_name="loan",
            name="given_by",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="loan",
            name="loan_type",
            field=models.CharField(
                choices=[("Given Out", "Given Out"), ("Received", "Received")],
                max_length=255,
                null=True,
            ),
        ),
    ]
