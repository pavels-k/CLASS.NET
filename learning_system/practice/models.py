from django.db import models

from learning_system.theory.models import Course


class PracticeCategory(models.Model):
    parent = models.ForeignKey('self',
                               blank=True,
                               null=True,
                               related_name='childrens',
                               on_delete=models.CASCADE,
                               verbose_name='')
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               verbose_name='Учебный предмет')

    class Meta:
        verbose_name = 'раздел практического материала'
        verbose_name_plural = 'разделы практического материала'

    def __str__(self):
        return str(self.pk)

    def has_read_permission(self):
        if self.user.is_authenticated:
            return True
        return False

    def has_object_read_permission(self, request):
        if self.user.is_authenticated:
            return True
        return False

    def has_write_permission(self):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False

    def has_object_write_permission(self, request):
        if request.user.is_authenticated:
            if (request.user.is_staff == True):
                return True
        return False

    def has_create_permission(self):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False



class AbstractTask(models.Model):
    class Task:
        TESTING = 1
        SELF_EDUCATION = 2
        CONTROLING = 3
        TASK_TYPES = ((TESTING, 'Тестовая'), (SELF_EDUCATION, 'Самообучение'),
                      (CONTROLING, 'Контролирующая'))

    task_type = models.CharField(choices=Task.TASK_TYPES,
                                 default=Task.TESTING,
                                 max_length=50,
                                 verbose_name='Тип задачи')
    content = models.CharField(max_length=50, verbose_name='Текста задачи')
    complexity = models.CharField(max_length=50,
                                  verbose_name='Сложность задачи')
    category = models.ForeignKey(PracticeCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name='Практический материал')
    status = models.CharField(max_length=1,
                              choices=(('C', 'Correct'),
                                       ('P', 'Partially correct'), ('W',
                                                                    'Wrong')),
                              verbose_name='Статус ответа')
    tries_count = models.IntegerField(default=0, verbose_name='Число попыток')
    user_answer = models.CharField(max_length=50,
                                   verbose_name='Ответ пользователя')
    correct_answer = models.CharField(max_length=50,
                                      verbose_name='Правильный ответ')

    class Meta:
        abstract = True
        verbose_name = 'практическое задание'
        verbose_name_plural = 'практические задания'

    def __str__(self):
        return str(self.pk)

    def has_read_permission(self):
        if self.user.is_authenticated:
            return True
        return False

    def has_object_read_permission(self, request):
        if self.user.is_authenticated:
            return True
        return False

    def has_write_permission(self):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False

    def has_object_write_permission(self, request):
        if request.user.is_authenticated:
            if (request.user.is_staff == True):
                return True
        return False

    def has_create_permission(self):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False

class FormulInputTask(AbstractTask):
    pass

class FormulInputTaskVariation(models.Model):
    param1 = models.IntegerField()
    param2 = models.IntegerField()
    task = models.ForeignKey(FormulInputTask, on_delete=models.CASCADE)

    
'''
class TaskUserData(models.Model):
    
    practice_task = models.ForeignKey(AbstractTask,
                                      on_delete=models.CASCADE,
                                      verbose_name='Практическое задание')
    
    status = models.CharField(max_length=1,
                              choices=(('C', 'Correct'),
                                       ('P', 'Partially correct'), ('W',
                                                                    'Wrong')),
                              verbose_name='Статус ответа')
    tries_count = models.IntegerField(default=0, verbose_name='Число попыток')
    user_answer = models.CharField(max_length=50,
                                   verbose_name='Ответ пользователя')
    correct_answer = models.CharField(max_length=50,
                                      verbose_name='Правильный ответ')

    class Meta:
        verbose_name = 'состояние практического задания'
        verbose_name_plural = 'состояния практических заданий'

    def add_new_try(self):
        self.tries_count += 1
        # self.state = PracticeTask.
        # self.user_answer = None
        self.save()

    def __str__(self):
        return str(self.pk)

    def has_read_permission(self):
        if self.user.is_authenticated:
            return True
        return False

    def has_object_read_permission(self, request):
        if self.user.is_authenticated:
            return True
        return False

    def has_write_permission(self):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False

    def has_object_write_permission(self, request):
        if request.user.is_authenticated:
            if (request.user.is_staff == True):
                return True
        return False

    def has_create_permission(self):
        if self.user.is_authenticated:
            if (self.user.is_staff == True):
                return True
        return False
'''
