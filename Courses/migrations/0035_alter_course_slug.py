# Generated by Django 5.0.6 on 2024-11-03 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0034_alter_articles_image_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
