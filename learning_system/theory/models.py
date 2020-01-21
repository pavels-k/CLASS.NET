from django.conf import settings
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название предмета')

class TheoryPost(models.Model):
    content = models.CharField(max_length=50, verbose_name='Аттрибут текста материала')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Учебный предмет')
    
class TheoryCategory(models.Model):
    # добавить в схему
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE) 
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Учебный предмет') 
    theorypost = models.ForeignKey(TheoryPost, on_delete=models.CASCADE, verbose_name='Теоретический материал') 
