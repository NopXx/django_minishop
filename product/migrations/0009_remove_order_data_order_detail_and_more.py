# Generated by Django 4.1.5 on 2023-02-07 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_order_detail_detail_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_data',
            name='order_detail',
        ),
        migrations.RemoveField(
            model_name='order_detail',
            name='detail_number',
        ),
        migrations.AddField(
            model_name='order_detail',
            name='order_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
