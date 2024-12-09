# Generated by Django 5.0.6 on 2024-11-12 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0004_remove_subcategory_passed_subcategory_avg_passed_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.RemoveField(
            model_name='answer',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='question',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='question',
            name='date_time',
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='duration',
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='result',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, to='QuizApp.useremail'),
        ),
    ]
