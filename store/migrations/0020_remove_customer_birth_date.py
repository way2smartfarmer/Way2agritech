# Generated by Django 4.1.7 on 2023-03-08 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_remove_customer_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='birth_date',
        ),
    ]
