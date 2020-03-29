from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.title

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
