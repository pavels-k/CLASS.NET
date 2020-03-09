from django.db import models

from learning_system.courses.models import Course


class TheoryCategory(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='childrens', on_delete=models.CASCADE,
                               verbose_name='Подраздел')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Учебный предмет')

    class Meta:
        verbose_name = 'раздел теоретического материала'
        verbose_name_plural = 'разделы теоретического материала'

    def __str__(self):
        return str(self.pk)


class TheoryPost(models.Model):
    content = models.CharField(max_length=50, verbose_name='Атрибут текста материала')
    category = models.ForeignKey(TheoryCategory, on_delete=models.CASCADE,
                                 verbose_name='Раздел теоретического материала')

    class Meta:
        verbose_name = 'теоретический материал'
        verbose_name_plural = 'теоретические материалы'

    def __str__(self):
        return str(self.pk)