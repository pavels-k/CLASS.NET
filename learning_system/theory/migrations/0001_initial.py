# Generated by Django 2.0.13 on 2020-01-20 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudySubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TheoryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_studysubject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theory.StudySubject')),
            ],
        ),
        migrations.CreateModel(
            name='TheoryPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('id_studysubject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theory.StudySubject')),
            ],
        ),
        migrations.AddField(
            model_name='theorycategory',
            name='id_theorypost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theory.TheoryPost'),
        ),
        migrations.AddField(
            model_name='theorycategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='theory.TheoryCategory'),
        ),
    ]
