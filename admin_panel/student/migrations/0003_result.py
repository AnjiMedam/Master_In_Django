# Generated by Django 5.1.6 on 2025-02-18 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_profile_roll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_class', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
