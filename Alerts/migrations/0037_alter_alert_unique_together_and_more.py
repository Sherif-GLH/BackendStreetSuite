# Generated by Django 5.0.6 on 2024-08-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alerts', '0036_alert_date_alert_time_alter_alert_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='alert',
            unique_together={('ticker', 'strategy', 'result_value', 'date')},
        ),
        migrations.AddIndex(
            model_name='alert',
            index=models.Index(fields=['ticker', 'strategy', 'result_value', 'date'], name='Alerts_aler_ticker__510ab7_idx'),
        ),
        migrations.RemoveField(
            model_name='alert',
            name='time_posted',
        ),
    ]
