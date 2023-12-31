# Generated by Django 3.1.14 on 2023-01-21 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20230121_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='buying_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='design_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='finance_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='fit_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='operations_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='pd_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='planning_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='rm_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='sourcing_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
