# Generated by Django 4.1.5 on 2023-01-24 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cart',
            new_name='cart_add',
        ),
    ]
