# Generated by Django 4.1.7 on 2023-05-28 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lipia', '0005_merge_0003_mpesaauthtoken_0004_mpesatransaction'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MpesaAuthToken',
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='ussd_code',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
