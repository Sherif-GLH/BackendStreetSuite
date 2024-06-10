# Generated by Django 5.0.6 on 2024-06-10 12:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0016_quizzes_questions_counter'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='quizzes',
            options={},
        ),
        migrations.AddField(
            model_name='quizzes',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='quizzes',
            name='image',
            field=models.ImageField(blank=True, default='QuizPic/default.png', null=True, upload_to='QuizPic/'),
        ),
    ]