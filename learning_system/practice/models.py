from django.conf import settings
from django.db import models
from ..theory.models import StudySubject

class PracticeType(models.Model):
    article_id = models.AutoField(primary_key=True)

class PracticeTask(models.Model):
    content = models.CharField(max_length=50)
    complexity = models.CharField(max_length=50)
    type_task = models.CharField(max_length=50) # изменить в схеме

class PracticeTaskVariation(models.Model):
    # убрать task в схеме
    id_practicetask = models.ForeignKey(PracticeTask, on_delete=models.CASCADE)

class PracticeCategory(models.Model):
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE) 
    id_studysubject = models.ForeignKey(StudySubject, on_delete=models.CASCADE) 
    id_practicetask = models.ForeignKey(PracticeTask, on_delete=models.CASCADE)