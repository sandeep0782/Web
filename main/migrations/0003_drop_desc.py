# Generated by Django 3.1.14 on 2022-12-01 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_season_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='drop',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]