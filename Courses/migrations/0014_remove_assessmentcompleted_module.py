# Generated by Django 5.0.6 on 2024-08-07 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0013_remove_articles_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessmentcompleted',
            name='module',
        ),
    ]