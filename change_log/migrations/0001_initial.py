<<<<<<< HEAD
# Generated by Django 5.0.6 on 2024-07-14 13:59
=======
# Generated by Django 5.0.6 on 2024-07-14 13:23
>>>>>>> d470e4e6f9714196466bef3aedeb414d35308634

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_message', models.TextField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
