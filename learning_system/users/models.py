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
    
    def create(self, **kwargs):
        kwargs.update({'role': 'S'})
        return super(StudentManager, self).create(**kwargs)

class TeacherManager(models.Manager):
    def get_queryset(self):
        return super(TeacherManager, self).get_queryset().filter(role='T')

    def create(self, **kwargs):
        kwargs.update({'role': 'T'})
        return super(TeacherManager, self).create(**kwargs)

class Student(User):
    objects = StudentManager()
    class Meta:
        proxy = True

class Teacher(User):
    objects = TeacherManager()
    class Meta:
        proxy = True
    
class Group(models.Model):
    user = models.ManyToManyField(User, verbose_name='Пользователь')
    name = models.CharField(max_length=50, verbose_name='Название курса')
    date_of_creation = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    available_subjects = models.ManyToManyField("self", verbose_name='Доступные предметы')
    
def  group_validate(self):
    if (self.role == Group.user) and (self.groups.all().count() > 0):
        raise ValidationError("Студент может быть только в одной группе")
    try:
        self.User.full_clean()
    except ValidationError as e:
        print('we have an error')
    

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь') # дополнить схему
    score = models.IntegerField(verbose_name='Количество очков')
    answers = models.CharField(max_length=100, verbose_name='Ответы')
    practicetask = models.ForeignKey(PracticeTask, on_delete=models.CASCADE, verbose_name='Задача')
