from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from learning_system.users.models import Student, StudyGroup, StudentProgress, Teacher
from learning_system.courses.models import Course
from learning_system.users.permission import IsTeacherOrAdmin

from learning_system.users.views.user_api import UserCreateView
from learning_system.users.serializers.student import StudentListSerializer, ProgressSerializer
from learning_system.users.serializers.teacher import TeacherCreateSerializer, TeacherListSerializer


class TeacherView(UserCreateView):
    serializer_class = TeacherCreateSerializer
    queryset = Teacher.objects.all()

class TeacherListView(viewsets.ModelViewSet):
    serializer_class = TeacherListSerializer
    queryset = Teacher.objects.all()