# Generated by Django 3.1.14 on 2022-12-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20221219_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otb',
            name='amount',
        ),
        migrations.AddField(
            model_name='otb',
            name='otb_consumed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='otb',
            name='total_otb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
