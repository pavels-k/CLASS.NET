# Generated by Django 2.0.13 on 2020-01-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200121_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='answers',
        ),
        migrations.AddField(
            model_name='user',
            name='studygroup',
            field=models.ManyToManyField(to='users.StudyGroup'),
        ),
    ]