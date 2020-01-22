from django.conf import settings
from django.db import models
from learning_system.theory.models import Course

class PracticeType(models.Model):
    article = models.AutoField(primary_key=True, verbose_name='Тип задачи')

class PracticeCategory(models.Model):
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE, verbose_name='') 
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Учебный предмет') 

class PracticeTask(models.Model):
    content = models.CharField(max_length=50, verbose_name='Текста задачи')
    complexity = models.CharField(max_length=50, verbose_name='Сложность задачи')
    type_task = models.CharField(max_length=50, verbose_name='Тип задачи') # изменить в схеме
    practicecategory = models.ForeignKey(PracticeCategory, on_delete=models.CASCADE, verbose_name='Практический материал')

class PracticeTaskVariation(models.Model):
    # убрать task в схеме
    practicetask = models.ForeignKey(PracticeTask, on_delete=models.CASCADE, verbose_name='Класс задачи')

    