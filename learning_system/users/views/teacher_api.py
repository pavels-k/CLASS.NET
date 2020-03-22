from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from learning_system.users.models import Student, StudyGroup, StudentProgress, Teacher
from learning_system.courses.models import Course
from learning_system.users.permission import IsTeacherOrAdmin

from learning_system.users.views.user_api import UserCreateView
from learning_system.users.serializers.student import StudentListSerializer, ProgressSerializer
from learning_system.users.serializers.teacher import TeacherCreateSerializer, \
    TeacherListSerializer, \
    SetStudentGroupSerializer, \
    StudentSelectSerializer, \
    ResultSerializer


#8
class TeacherCreateView(UserCreateView):
    serializer_class = TeacherCreateSerializer
    queryset = Teacher.objects.all()
#9
class TeacherView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TeacherListSerializer
    queryset = Teacher.objects.all()

#16
class SetGroupView(viewsets.ModelViewSet):
    serializer_class = SetStudentGroupSerializer
    queryset = Student.objects.all()
    permission_classes = [IsTeacherOrAdmin]

#18
class GroupSelectView(generics.ListAPIView):
    serializer_class = StudentSelectSerializer
    queryset = Student.objects.all()
    permission_classes = [IsTeacherOrAdmin]

    def list(self, request, pk):
        id = pk
        if id == 'None':
            content = {'You did not select a group'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        study_group = StudyGroup.objects.filter(id=id)[:1]
        students = Student.objects.filter(study_group=study_group)
        students_progress = StudentProgress.objects.none()
        for student in students:
            students_progress |= StudentProgress.objects.filter(
                student=student)
        serializer = ResultSerializer(students_progress, many=True) # исправить
        return Response(serializer.data)

#20
class StudentResultList(generics.ListAPIView):
    serializer_class = StudentListSerializer
    queryset = Student.objects.all()
    permission_classes = [IsTeacherOrAdmin]

    def list(self, request):
        queryset = self.get_queryset()
        group = self.request.query_params.get('group', None)
        course = self.request.query_params.get('course', None)
        if group and course:
            course = get_object_or_404(Course, pk=course)
            group = get_object_or_404(StudyGroup, pk=group)
            if course in group.available_subjects.all():
                queryset = queryset.filter(study_group=group)
            else:
                queryset = queryset.none()
            serializer = ProgressSerializer(queryset,
                                            many=True,
                                            context={'course': course})
        return Response(serializer.data)