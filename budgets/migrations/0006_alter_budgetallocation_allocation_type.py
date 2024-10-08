# Generated by Django 5.1.1 on 2024-10-07 08:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("budgets", "0005_budgetallocation_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="budgetallocation",
            name="allocation_type",
            field=models.CharField(
                choices=[
                    ("Rent", "Rent"),
                    ("Household", "Household"),
                    ("Food", "Food"),
                    ("Commuting", "Commuting"),
                    ("Family", "Family"),
                    ("Loan Repayments", "Loan Repayments"),
                    ("Entertainment", "Entertainment"),
                    ("Charity and Support", "Charity and Support"),
                    ("Investments", "Investments"),
                    ("Savings", "Savings"),
                    ("Personal Use", "Personal Use"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]
