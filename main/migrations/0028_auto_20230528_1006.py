# Generated by Django 3.1.14 on 2023-05-28 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20230528_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_management',
            name='app',
        ),
        migrations.RemoveField(
            model_name='order_management',
            name='asp',
        ),
    ]
