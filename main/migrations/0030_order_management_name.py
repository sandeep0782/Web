# Generated by Django 3.1.14 on 2023-05-28 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20230528_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_management',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
