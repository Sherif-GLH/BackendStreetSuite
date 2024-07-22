# Generated by Django 5.0.6 on 2024-07-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alerts', '0024_alert_insiderbuyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert_insiderbuyer',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='alert_insiderbuyer',
            name='strategy_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='alert_insiderbuyer',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='alert_insiderbuyer',
            name='buyer_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='alert_insiderbuyer',
            name='job_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='alert_insiderbuyer',
            name='transaction_type',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
