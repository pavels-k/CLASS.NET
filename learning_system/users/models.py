from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from ..practice.models import PracticeTask


class User(AbstractUser):
    #surname = models.CharField(max_length=50)
    #name = models.CharField(max_length=50)
    #patronymic = models.CharField(max_length=50)
    #id_abstractuser = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    pass

class Student(models.Model):
     id_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class Teacher(models.Model):
     id_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class Moderator(models.Model): # отсутствует в схеме
     id_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class StudyGroup(models.Model):
    name = models.CharField(max_length=50)
    date_of_creation = models.DateTimeField(default=timezone.now)
    id_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    id_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    available_subjects = models.ManyToManyField("self")

class UserProgress(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE) # дополнить схему
    score = models.IntegerField()
    answers = models.CharField(max_length=100)
    id_practicetask = models.ForeignKey(PracticeTask, on_delete=models.CASCADE)
