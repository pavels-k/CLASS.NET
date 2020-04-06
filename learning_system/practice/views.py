from rest_framework import generics, viewsets
from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import action
from rest_framework.response import Response

from learning_system.practice.models import AbstractTask, PracticeCategory
from learning_system.practice.serializers import \
    PracticeCategoryCreateSerializer, \
    PracticeTaskCreateSerializer, \
    PracticeCategorySerializer, \
    PracticeTaskSerializer
from learning_system.users.models import StudentProgress
from learning_system.users.models import StudyGroup, Student
from learning_system.courses.models import Course
from learning_system.users.permission import IsAdminUser, IsStudent
from dry_rest_permissions.generics import DRYPermissions


class PracticeCategoryView(viewsets.ModelViewSet):
    serializer_class = PracticeCategoryCreateSerializer
    permission_classes = (DRYPermissions,)
    queryset = PracticeCategory.objects.all()

'''
class PracticeTaskView(viewsets.ModelViewSet):
    serializer_class = PracticeTaskCreateSerializer
    permission_classes = (DRYPermissions,)
    queryset = AbstractTask.objects.all()

    @action(detail=False, methods=['get'], permission_classes=[IsStudent])
    def student_task(self, request):
        student_progress = get_object_or_404(StudentProgress,
                                             student=request.user)
        practice_task = student_progress.practice_task
        serializer = self.serializer_class(practice_task)
        return Response(serializer.data)


class TaskUserDataView(viewsets.ModelViewSet):
    serializer_class = TaskUserDataCreateSerializer
    permission_classes = [IsAdminUser]
    queryset = TaskUserData.objects.all()
'''


