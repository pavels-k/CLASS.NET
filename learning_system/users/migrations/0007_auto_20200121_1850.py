# Generated by Django 2.0.13 on 2020-01-21 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200121_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprogress',
            name='answers',
            field=models.CharField(max_length=100, verbose_name='Ответы'),
        ),
        migrations.AlterField(
            model_name='userprogress',
            name='practicetask',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.PracticeTask', verbose_name='Задача'),
        ),
        migrations.AlterField(
            model_name='userprogress',
            name='score',
            field=models.IntegerField(verbose_name='Количество очков'),
        ),
    ]
