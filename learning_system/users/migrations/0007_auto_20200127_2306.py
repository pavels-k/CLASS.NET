# Generated by Django 2.0.13 on 2020-01-27 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_reviewsonteacher_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewsonteacher',
            name='reviews',
            field=models.TextField(verbose_name='Отзывы на преподавателей'),
        ),
    ]
