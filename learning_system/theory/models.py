from django.conf import settings
from django.db import models

class StudySubject(models.Model):
    title = models.CharField(max_length=50)

class TheoryPost(models.Model):
    content = models.CharField(max_length=50)
    id_studysubject = models.ForeignKey(StudySubject, on_delete=models.CASCADE)
    
class TheoryCategory(models.Model):
    # добавить в схему
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE) 
    id_studysubject = models.ForeignKey(StudySubject, on_delete=models.CASCADE) 
    id_theorypost = models.ForeignKey(TheoryPost, on_delete=models.CASCADE) 
