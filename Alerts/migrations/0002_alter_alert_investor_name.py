# Generated by Django 5.0.6 on 2025-04-06 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alerts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='investor_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
