# Generated by Django 4.1.7 on 2023-03-08 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_remove_customer_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
