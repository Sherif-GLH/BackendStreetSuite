# Generated by Django 5.0.6 on 2024-06-10 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0013_rename_text_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='text',
        ),
    ]