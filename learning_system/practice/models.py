from django.conf import settings
from django.db import models
from learning_system.theory.models import Course
#from learning_system.users.models import Student


class PracticeCategory(models.Model):
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='childrens', on_delete=models.CASCADE, verbose_name='') 
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Учебный предмет') 

class PracticeTask(models.Model):
    content = models.CharField(max_length=50, verbose_name='Текста задачи')
    complexity = models.CharField(max_length=50, verbose_name='Сложность задачи')
    type_task = models.CharField(max_length=50, verbose_name='Тип задачи') # изменить в схеме
    category = models.ForeignKey(PracticeCategory, on_delete=models.CASCADE, verbose_name='Практический материал')
    #student = models.ManyToManyField('users.Student', through='TaskUserData')

class TaskUserData(models.Model):
    #student = models.ForeignKey('users.Student', on_delete=models.CASCADE, verbose_name='Студент')
    practicetask = models.ForeignKey(PracticeTask, on_delete=models.CASCADE, verbose_name='Практическое задание')
    status = models.CharField(max_length=1, choices=(('C', 'Correct'),('P', 'Partially correct'),('W', 'Wrong')), verbose_name='Статус ответа')
    tries_count = models.IntegerField(default = 0, verbose_name='Чило попыток')
    user_answer = models.CharField(max_length=50, verbose_name='Ответ пользователя') 
    correct_answer = models.CharField(max_length=50, verbose_name='Правильный ответ')
    params = models.CharField(max_length=50, verbose_name='')
    def add_new_try(self):
        self.tries_count += 1
        #self.state = PracticeTask.
        #self.user_answer = None
        self.save()



'''
class PracticeType(models.Model):
    article = models.AutoField(primary_key=True, verbose_name='Тип задачи')

class PracticeTaskVariation(models.Model):
    # убрать task в схеме
    practicetask = models.ForeignKey(PracticeTask, on_delete=models.CASCADE, verbose_name='Класс задачи')
'''
    