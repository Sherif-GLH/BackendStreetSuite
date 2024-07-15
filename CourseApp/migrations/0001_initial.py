<<<<<<< HEAD
# Generated by Django 5.0.6 on 2024-07-14 13:59
=======
# Generated by Django 5.0.6 on 2024-07-14 13:23
>>>>>>> d470e4e6f9714196466bef3aedeb414d35308634

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('instructions', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='CoursePic/default.png', null=True, upload_to='CoursePic/')),
                ('title', models.CharField(max_length=255)),
                ('likes_number', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=12, null=True)),
                ('subscriber_number', models.PositiveIntegerField(default=0)),
                ('completed', models.PositiveIntegerField(default=0)),
                ('duration', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=32)),
                ('time_to_complete', models.IntegerField(null=True)),
                ('likes', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('subscribed', models.ManyToManyField(related_name='subscribed', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses_author', to=settings.AUTH_USER_MODEL)),
                ('users_completed', models.ManyToManyField(related_name='Course', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='CourseApp.course')),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentCompleted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessment_completed', to='CourseApp.assessment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assment_completed', to=settings.AUTH_USER_MODEL)),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed', to='CourseApp.module')),
            ],
        ),
        migrations.AddField(
            model_name='assessment',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='CourseApp.module'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='CourseApp.assessment')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='CourseApp.question')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('article', models.TextField()),
                ('image', models.ImageField(blank=True, default='CoursePic/default.png', null=True, upload_to='CoursePic/SectionPic/')),
                ('completed', models.ManyToManyField(related_name='section_completed', to=settings.AUTH_USER_MODEL)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CourseApp.module')),
            ],
        ),
    ]
