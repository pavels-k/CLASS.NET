# Generated by Django 2.0.13 on 2020-02-08 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicetask',
            name='student',
        ),
        migrations.RemoveField(
            model_name='taskuserdata',
            name='student',
        ),
    ]
