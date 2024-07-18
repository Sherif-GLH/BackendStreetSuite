# Generated by Django 5.0.6 on 2024-07-17 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alerts', '0007_social_media_mentions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts_details',
            name='risk_level',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alerts_details',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
        
    ]