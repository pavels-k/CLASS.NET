from rest_framework import generics, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
from learning_system.users.models import StudentProgress, ReviewsOnTeacher, Student, StudyGroup
from learning_system.users.views.user_api import UserCreateView
from learning_system.practice.models import PracticeCategory, PracticeTask
from learning_system.users.permission import IsStudent, IsAdminUser
from learning_system.users.models import Student, StudyGroup, StudentProgress, ReviewsOnTeacher

from learning_system.users.serializers.student import StudentCreateSerializer, \
    StudyGroupCreateSerializer, \
    StudyGroupListSerializer, \
    StudentProgressCreateSerializer, \
    ReviewsOnTeacherCreateSerializer, \
    StudentProgressSerializer, \
    ReviewsOnTeacherSerializer, \
    StudentListSerializer, \
    GetTaskListSerializer, \
    ProgressSerializer

#1
class StudyGroupCreateView(viewsets.ModelViewSet):
    serializer_class = StudyGroupCreateSerializer
    queryset = StudyGroup.objects.all()
#2
class StudyGroupView(viewsets.ReadOnlyModelViewSet):
    serializer_class = StudyGroupListSerializer
    queryset = StudyGroup.objects.all()

#6
class StudentCreateView(UserCreateView):
    serializer_class = StudentCreateSerializer
    queryset = Student.objects.all()
#7
class StudentView(viewsets.ReadOnlyModelViewSet):
    serializer_class = StudentListSerializer
    queryset = Student.objects.all()

#10
class StudentProgressCreateView(viewsets.ModelViewSet):
    serializer_class = StudentProgressCreateSerializer
    queryset = StudentProgress.objects.all()
    permission_classes = [IsAdminUser]

#11
class StudentProgressView(viewsets.ReadOnlyModelViewSet):
    serializer_class = StudentProgressSerializer
    queryset = StudentProgress.objects.all()

#17
class GetTaskListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = GetTaskListSerializer
    queryset = PracticeTask.objects.all()
    permission_classes = [IsStudent]

    def list(self, request):
        student_progress = get_object_or_404(StudentProgress,
                                             student=request.user)
        practice_task = student_progress.practice_task
        serializer = self.serializer_class(practice_task)
        return Response(serializer.data)



#14
class ReviewsOnTeacherCreateView(viewsets.ModelViewSet):
    serializer_class = ReviewsOnTeacherCreateSerializer
    queryset = ReviewsOnTeacher.objects.all()

#15
class ReviewsOnTeacherView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReviewsOnTeacherSerializer
    queryset = ReviewsOnTeacher.objects.all()