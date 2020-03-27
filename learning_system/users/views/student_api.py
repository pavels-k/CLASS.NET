from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from learning_system.users.models import StudentProgress, ReviewsOnTeacher, Student, StudyGroup
from learning_system.users.views.user_api import UserCreateView
from learning_system.users.permission import IsStudent, IsAdminUser, IsTeacherOrAdmin
from learning_system.users.models import Student, StudyGroup, StudentProgress, ReviewsOnTeacher
from learning_system.courses.models import Course
from dry_rest_permissions.generics import DRYPermissions
from learning_system.users.serializers.student import StudentCreateSerializer, \
    StudyGroupCreateSerializer, \
    StudentProgressCreateSerializer, \
    ReviewsOnTeacherCreateSerializer, \
    StudentListSerializer, \
    ProgressSerializer, \
    StudentUpdateGroupeSerializer, \
    ResultSerializer


class StudyGroupView(viewsets.ModelViewSet):
    permission_classes = (DRYPermissions, )
    serializer_class = StudyGroupCreateSerializer
    queryset = StudyGroup.objects.all()


class StudentView(UserCreateView):
    permission_classes = (DRYPermissions, )
    serializer_class = StudentCreateSerializer
    queryset = Student.objects.all()
    action_serializers = {
        'list': StudentListSerializer,
        'retrieve': StudentListSerializer,
        'create': StudentCreateSerializer,
        'update': StudentUpdateGroupeSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]

        return self.serializer_class

    @action(detail=False, methods=['get'])
    def list_task(self, request):
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


class StudentProgressView(viewsets.ModelViewSet):
    serializer_class = StudentProgressCreateSerializer
    queryset = StudentProgress.objects.all()
    permission_classes = (DRYPermissions, )

    @action(detail=True,
            methods=['get'],
            permission_classes=[IsTeacherOrAdmin])
    def list_study_group_results(self, request, pk):
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
        serializer = ResultSerializer(students_progress, many=True)
        return Response(serializer.data)


class ReviewsOnTeacherCreateView(viewsets.ModelViewSet):
    serializer_class = ReviewsOnTeacherCreateSerializer
    queryset = ReviewsOnTeacher.objects.all()
    permission_classes = (DRYPermissions, )
