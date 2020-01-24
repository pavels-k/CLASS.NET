from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from learning_system.practice.models import PracticeTask
from django.core.exceptions import ValidationError
    
class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField('users.Group', related_name="groups")
    role = models.CharField(max_length=1, choices=(('S', 'Student'),('T', 'Teacher'),))

class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(role='S')
    

class TeacherManager(models.Manager):
    def get_queryset(self):
        return super(TeacherManager, self).get_queryset().filter(role='T')

class Student(User):
    objects = StudentManager()
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        self.role = 'S'
        super(Student, self).save(*args, **kwargs)

class Teacher(User):
    objects = TeacherManager()
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        self.role = 'T'
        super(Teacher, self).save(*args, **kwargs)
        
    
class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название курса')
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    available_subjects = models.ManyToManyField("self", verbose_name='Доступные предметы')
    
def  group_validate(self):
    if (self.role == "S") and (self.groups.all().count() > 1):
        raise ValidationError("Студент может быть только в одной группе")
        try:
            self.clean()
        except ValidationError as e:
            print('we have an error')
    

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь') # дополнить схему
    score = models.IntegerField(verbose_name='Количество очков')
    answers = models.CharField(max_length=100, verbose_name='Ответы')
    practicetask = models.ForeignKey(PracticeTask, on_delete=models.CASCADE, verbose_name='Задача')
    
