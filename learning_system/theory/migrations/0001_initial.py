# Generated by Django 2.2 on 2020-03-05 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheoryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Учебный предмет')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='theory.TheoryCategory', verbose_name='Подраздел')),
            ],
            options={
                'verbose_name': 'раздел теоретического материала',
                'verbose_name_plural': 'разделы теоретического материала',
            },
        ),
        migrations.CreateModel(
            name='TheoryPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50, verbose_name='Атрибут текста материала')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theory.TheoryCategory', verbose_name='Раздел теоретического материала')),
            ],
            options={
                'verbose_name': 'теоретический материал',
                'verbose_name_plural': 'теоретические материалы',
            },
        ),
    ]
