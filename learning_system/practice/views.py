from rest_framework import generics

from .models import TaskUserData, PracticeTask, PracticeCategory
from .serializers import \
    PracticeCategoryCreateSerializer, \
    PracticeTaskCreateSerializer, \
    TaskUserDataCreateSerializer, \
    PracticeCategorySerializer, \
    PracticeTaskSerializer, GetTaskListSerializer, \
    TaskUserDataSerializer
from learning_system.users.serializers import StudentProgressSerializer
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
'''
class GetPracticeForStudents(generics.ListAPIView):
    serializer_class = PracticeTaskSerializer
    queryset = PracticeTask.objects.all()
    
    def task_for_students(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            student_id = request.user.get('id')
'''
class GetTaskListView(generics.CreateAPIView):
    serializer_class = GetTaskListSerializer
    #queryset = Student.objects.all()
            