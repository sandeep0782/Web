# Generated by Django 3.1.14 on 2023-01-21 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20230121_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.buyer'),
        ),
    ]
