from django.conf import settings
from django.db import models
from learning_system.courses.models import Course


    
class TheoryCategory(models.Model):
    # добавить в схему
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE) 
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Учебный предмет') 

class TheoryPost(models.Model):
    content = models.CharField(max_length=50, verbose_name='Аттрибут текста материала')
    theorycategory =  models.ForeignKey(TheoryCategory, on_delete=models.CASCADE, verbose_name='Теоретический материал')

