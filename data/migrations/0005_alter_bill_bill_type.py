# Generated by Django 4.1.1 on 2022-11-13 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_bill_bill_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_type',
            field=models.CharField(max_length=255),
        ),
    ]
