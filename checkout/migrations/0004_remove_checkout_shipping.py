# Generated by Django 4.2.16 on 2024-12-09 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_remove_checkout_car_remove_checkout_prod_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='shipping',
        ),
    ]