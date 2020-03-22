from rest_framework import generics

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

class PracticeCategoryCreateView(generics.CreateAPIView):
    serializer_class = PracticeCategoryCreateSerializer


class PracticeTaskCreateView(generics.CreateAPIView):
    serializer_class = PracticeTaskCreateSerializer


class TaskUserDataCreateView(generics.CreateAPIView):
    serializer_class = TaskUserDataCreateSerializer


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

class GetTaskListView(generics.CreateAPIView):
    serializer_class = GetTaskListSerializer

            