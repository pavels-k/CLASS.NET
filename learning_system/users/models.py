from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from dry_rest_permissions.generics import allow_staff_or_superuser

from learning_system.courses.models import Course
from learning_system.practice.models import PracticeTask


class User(AbstractUser):
    is_staff = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    role = models.CharField(max_length=1,
                            choices=(
                                ('S', 'Student'),
                                ('T', 'Teacher'),
                            ))


class Student(User):
    study_group = models.ForeignKey('users.StudyGroup',
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True,
                                    related_name='students',
                                    verbose_name='Учебная группа')

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'

    def save(self, *args, **kwargs):
        self.role = 'S'
        super(Student, self).save(*args, **kwargs)

    def has_read_permission(self):
        return True

    def has_write_permission(self, request):
        if self.user.is_authenticated:
            if (self.user.is_staff == True) | (self.user.role == 'T'):
                return True
        return False

    def has_create_permission(self):
        if self.user.is_authenticated:
            if (self.user.is_staff == True) | (self.user.role == 'T'):
                return True
        return False


class Teacher(User):
    study_groups = models.ManyToManyField('users.StudyGroup',
                                          related_name='teachers',
                                          verbose_name='Учебные группы')

    class Meta:
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'

    def save(self, *args, **kwargs):
        self.role = 'T'
        super(Teacher, self).save(*args, **kwargs)

    def has_read_permission(self):
        return True

    def has_write_permission(self, request):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False

    def has_create_permission(self):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False


class StudyGroup(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    creation_date = models.DateTimeField(default=timezone.now,
                                         verbose_name='Дата создания')
    available_subjects = models.ManyToManyField(Course,
                                                verbose_name='Доступные курсы',
                                                blank=True)

    class Meta:
        verbose_name = 'учебная группа'
        verbose_name_plural = 'учебные группы'

    def __str__(self):
        return self.name

    def has_read_permission(self):
        return True

    def has_write_permission(self, request):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False

    def has_create_permission(self):
        if self.user.is_authenticated():
            if (self.user.is_staff == True):
                return True
        return False


class StudentProgress(models.Model):
    student = models.ForeignKey(Student,
                                on_delete=models.CASCADE,
                                verbose_name='Студент')
    score = models.IntegerField(verbose_name='Количество очков')
    answers = models.CharField(max_length=100, verbose_name='Ответы')
    practice_task = models.ForeignKey('practice.PracticeTask',
                                      on_delete=models.CASCADE,
                                      verbose_name='Задача')

    class Meta:
        verbose_name = 'прогресс студента'
        verbose_name_plural = 'прогрессы студентов'

    def __str__(self):
        return str(self.pk)

    def has_read_permission(self):
        return True

    def has_write_permission(self, request):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False

    def has_create_permission(self):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False


class UserComplaint(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    complaints = models.TextField(verbose_name='Содержание')

    class Meta:
        verbose_name = 'жалоба пользователя'
        verbose_name_plural = 'жалобы пользователей'

    def __str__(self):
        return str(self.pk)

    def has_read_permission(self):
        return True

    def has_write_permission(self, request):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False

    def has_create_permission(self):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False


class ReviewsOnTeacher(models.Model):
    student = models.ForeignKey(Student,
                                on_delete=models.CASCADE,
                                verbose_name='Студент')
    reviews = models.TextField(verbose_name='Содержание')
    fullname = models.CharField(max_length=100,
                                verbose_name='Ф.И.О. преподавателя')

    class Meta:
        verbose_name = 'отзыв на преподавателя'
        verbose_name_plural = 'отзывы на преподавателей'

    def __str__(self):
        return str(self.pk)

    def has_read_permission(self):
        return True

    def has_write_permission(self, request):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False

    def has_create_permission(self):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False
