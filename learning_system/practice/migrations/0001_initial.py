# Generated by Django 2.0.13 on 2020-01-20 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('theory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PracticeTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('complexity', models.CharField(max_length=50)),
                ('type_task', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PracticeTaskVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_practicetask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.PracticeTask')),
            ],
        ),
        migrations.CreateModel(
            name='PracticeType',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='practicecategory',
            name='id_practicetask',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.PracticeTask'),
        ),
        migrations.AddField(
            model_name='practicecategory',
            name='id_studysubject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theory.StudySubject'),
        ),
        migrations.AddField(
            model_name='practicecategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='practice.PracticeCategory'),
        ),
    ]