from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic.base import View
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from django.shortcuts import (get_object_or_404, redirect, render,
                              render_to_response)

from learning_system.users.models import StudentProgress, UserComplaint, ReviewsOnTeacher, Student, Teacher, StudyGroup
from learning_system.users.serializers import StudentCreateSerializer, \
    TeacherCreateSerializer, \
    UserCreateSerializer, \
    StudyGroupCreateSerializer, \
    UserLoginSerializer, \
    StudentProgressCreateSerializer, \
    UserComplaintCreateSerializer, \
    ReviewsOnTeacherCreateSerializer, \
    StudentProgressSerializer, \
    UserComplaintSerializer, \
    ReviewsOnTeacherSerializer, \
    StudentSerializer, \
    StudentMoveSerializer, \
    SetStudentGroupSerializer, \
    GetTaskListSerializer, \
    ResultSerializer, \
    StudentSelectSerializer, \
    AddCourseToStudyGroup, \
    StudyGroupSelectionSerializer, \
    ProgressSerializer
from .permission import IsStudent, IsTeacherOrAdmin, IsAdminUser
from learning_system.practice.models import PracticeCategory, PracticeTask
from learning_system.courses.models import Course


class StudyGroupCreateView(generics.CreateAPIView):
    serializer_class = StudyGroupCreateSerializer


class StudyGroupView(generics.ListAPIView):
    serializer_class = StudyGroupCreateSerializer
    queryset = StudyGroup.objects


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('users:login_user'))


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return Response('You are signed in successfully as %s' % user.username)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            username = request.data.get('username')
            password = request.data.get('password')
            authenticate(username=username, password=password)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentCreateView(UserCreateView):
    serializer_class = StudentCreateSerializer


class StudentView(generics.ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects
    #permission_classes = [IsStudent]

class TeacherCreateView(UserCreateView):
    serializer_class = TeacherCreateSerializer


class TeacherView(generics.ListAPIView):
    serializer_class = TeacherCreateSerializer
    queryset = Teacher.objects


class StudentProgressCreateView(generics.CreateAPIView):
    serializer_class = StudentProgressCreateSerializer


class StudentProgressView(generics.ListAPIView):
    serializer_class = StudentProgressSerializer
    queryset = StudentProgress.objects


class UserComplaintCreateView(generics.CreateAPIView):
    serializer_class = UserComplaintCreateSerializer


class UserComplaintView(generics.ListAPIView):
    serializer_class = UserComplaintSerializer
    queryset = UserComplaint.objects


class ReviewsOnTeacherCreateView(generics.CreateAPIView):
    serializer_class = ReviewsOnTeacherCreateSerializer


class ReviewsOnTeacherView(generics.ListAPIView):
    serializer_class = ReviewsOnTeacherSerializer
    queryset = ReviewsOnTeacher.objects


'''
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentMoveSerializer
    queryset = Student.objects
    permission_classes = [IsTeacherOrAdmin]
'''
    
class SetGroupView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SetStudentGroupSerializer
    queryset = Student.objects
    permission_classes = [IsTeacherOrAdmin]

class GetTaskListView(generics.ListAPIView):
    serializer_class = GetTaskListSerializer
    queryset = PracticeTask.objects
    permission_classes = [IsStudent]
    
    def get(self, request):
            student_progress = get_object_or_404(StudentProgress, student = request.user)
            practice_task = student_progress.practice_task
            serializer = self.serializer_class(practice_task)
            return Response(serializer.data)
'''
class GetResultsListView(generics.ListAPIView):
    serializer_class = ResultSerializer
    permission_classes = [IsTeacherOrAdmin]
'''
    
class GroupSelectView(generics.ListAPIView):
    serializer_class = StudentSelectSerializer
    queryset = Student.objects
    permission_classes = [IsTeacherOrAdmin]
    def list(self, request, pk):       
        id = pk
        if id == 'None':
            content = {'You did not select a group'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        study_group = StudyGroup.objects.filter(id = id)[:1]
        students = Student.objects.filter(study_group = study_group)
        students_progress = StudentProgress.objects.none()
        for student in students:
            students_progress |= StudentProgress.objects.filter(student = student)
        serializer = ResultSerializer(students_progress, many = True) 
        return Response(serializer.data)

    

#AddCourseToStudyGroup

class AddCourseToStudyGroupView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddCourseToStudyGroup
    queryset = StudyGroup.objects
    permission_classes = [IsAdminUser]
    #def post(self, request):
'''
class StudentSelectView(generics.CreateAPIView):
    serializer_class = StudyGroupSelectionSerializer
    queryset = StudyGroup.objects.all()
'''
class StudentResultList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsTeacherOrAdmin]
    
    def list(self, request):
        queryset = self.get_queryset()
        group = self.request.query_params.get('group', None)
        course = self.request.query_params.get('course', None)
        if group and course:
            course = get_object_or_404(Course, pk = course)
            group = get_object_or_404(StudyGroup, pk = group)
            if course in group.available_subjects.all():
                queryset = queryset.filter(study_group = group)
            else:
                queryset = queryset.none()
            print(queryset)
            serializer = ProgressSerializer(queryset, many = True, context = {'course': course})
        return Response(serializer.data)
