# Generated by Django 4.2.16 on 2024-11-18 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='tax',
        ),
    ]