# Generated by Django 5.0.6 on 2024-11-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0005_alter_question_options_remove_answer_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='users',
            field=models.ManyToManyField(blank=True, to='QuizApp.useremail'),
        ),
    ]
