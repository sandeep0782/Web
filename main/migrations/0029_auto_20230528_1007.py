# Generated by Django 3.1.14 on 2023-05-28 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20230528_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_management',
            name='total_inventory',
        ),
        migrations.RemoveField(
            model_name='order_management',
            name='total_return',
        ),
        migrations.RemoveField(
            model_name='order_management',
            name='total_sale',
        ),
        migrations.RemoveField(
            model_name='order_management',
            name='under_production',
        ),
    ]
