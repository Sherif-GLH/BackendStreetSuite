# Generated by Django 5.0.6 on 2024-11-11 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0041_answers_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='Courses.questions'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='assessment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='Courses.assessment'),
        ),
    ]
