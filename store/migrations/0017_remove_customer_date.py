# Generated by Django 4.1.7 on 2023-03-08 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_customer_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date',
        ),
    ]
