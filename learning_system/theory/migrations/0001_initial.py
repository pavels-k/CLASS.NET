# Generated by Django 2.0.13 on 2020-01-24 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheoryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Учебный предмет')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='theory.TheoryCategory')),
            ],
        ),
        migrations.CreateModel(
            name='TheoryPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50, verbose_name='Аттрибут текста материала')),
                ('theorycategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theory.TheoryCategory', verbose_name='Теоретический материал')),
            ],
        ),
    ]
