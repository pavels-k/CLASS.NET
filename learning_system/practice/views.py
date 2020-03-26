from rest_framework import generics, viewsets
from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import action
from rest_framework.response import Response

from learning_system.practice.models import TaskUserData, PracticeTask, PracticeCategory
from learning_system.practice.serializers import \
    PracticeCategoryCreateSerializer, \
    PracticeTaskCreateSerializer, \
    TaskUserDataCreateSerializer, \
    PracticeCategorySerializer, \
    PracticeTaskSerializer, GetTaskListSerializer, \
    TaskUserDataSerializer
from learning_system.users.models import StudentProgress
from learning_system.users.models import StudyGroup, Student
from learning_system.courses.models import Course
from learning_system.users.permission import IsAdminUser, IsStudent


class PracticeCategoryCreateView(generics.CreateAPIView):
    serializer_class = PracticeCategoryCreateSerializer
    permission_classes = [IsAdminUser]


class PracticeTaskCreateView(viewsets.ModelViewSet):
    serializer_class = PracticeTaskCreateSerializer
    permission_classes = [IsAdminUser]
    queryset = PracticeTask.objects.all()

    @action(detail=False, methods=['get'], permission_classes=[IsStudent])
    def student_task(self, request):
        student_progress = get_object_or_404(StudentProgress,
                                             student=request.user)
        practice_task = student_progress.practice_task
        serializer = self.serializer_class(practice_task)
        return Response(serializer.data)


class TaskUserDataCreateView(generics.CreateAPIView):
    serializer_class = TaskUserDataCreateSerializer
    permission_classes = [IsAdminUser]


class PracticeCategoryView(generics.ListAPIView):
    serializer_class = PracticeCategorySerializer
    queryset = PracticeCategory.objects


class PracticeTaskView(generics.ListAPIView):
    serializer_class = PracticeTaskSerializer
    queryset = PracticeTask.objects


class TaskUserDataView(generics.ListAPIView):
    serializer_class = TaskUserDataSerializer
    queryset = TaskUserData.objects


class PracticeTaskUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PracticeTaskSerializer
    queryset = PracticeTask.objects.all()
    permission_classes = [IsAdminUser]


class GetTaskListView(generics.CreateAPIView):
    serializer_class = GetTaskListSerializer
