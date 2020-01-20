from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Student(User):
    class Meta:
        proxy = True

class Moderator(User):
    class Meta:
        proxy = True

class Teacher(User):
    class Meta:
        proxy = True
