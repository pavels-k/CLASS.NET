# Generated by Django 2.0.13 on 2020-01-21 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0005_auto_20200121_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicecategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='practice.PracticeCategory', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='practicecategory',
            name='studysubject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theory.StudySubject', verbose_name='Учебный предмет'),
        ),
        migrations.AlterField(
            model_name='practicetask',
            name='complexity',
            field=models.CharField(max_length=50, verbose_name='Сложность задачи'),
        ),
        migrations.AlterField(
            model_name='practicetask',
            name='content',
            field=models.CharField(max_length=50, verbose_name='Текста задачи'),
        ),
        migrations.AlterField(
            model_name='practicetask',
            name='practicecategory',
            field=models.ForeignKey(default='SOME STRING', on_delete=django.db.models.deletion.CASCADE, to='practice.PracticeCategory', verbose_name='Практический материал'),
        ),
        migrations.AlterField(
            model_name='practicetask',
            name='type_task',
            field=models.CharField(max_length=50, verbose_name='Тип задачи'),
        ),
        migrations.AlterField(
            model_name='practicetaskvariation',
            name='practicetask',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.PracticeTask', verbose_name='Класс задачи'),
        ),
        migrations.AlterField(
            model_name='practicetype',
            name='article',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Тип задачи'),
        ),
    ]