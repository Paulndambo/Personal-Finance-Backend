# Generated by Django 4.1.1 on 2022-11-13 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0006_alter_bill_bill_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='budget',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_type',
            field=models.CharField(choices=[('basic', 'Basic'), ('family', 'Family'), ('luxury', 'Luxury'), ('investment', 'Investment'), ('other', 'Other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='bill',
            name='budget',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='data.budget'),
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('loan_type', models.CharField(choices=[('to', 'Loaned To Me'), ('from', 'From Me')], max_length=255)),
                ('amount_loaned', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_repaid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('loan_status', models.CharField(choices=[('paid', 'Paid'), ('paying', 'Paying'), ('defaulted', 'Defaulted')], max_length=255)),
                ('loan_date', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
