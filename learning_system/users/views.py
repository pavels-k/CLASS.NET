from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic.base import View
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from django.shortcuts import (get_object_or_404, redirect, render,
                              render_to_response)

from .models import StudentProgress, UserComplaint, ReviewsOnTeacher, Student, Teacher, StudyGroup
from .serializers import StudentCreateSerializer, \
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
    GetTaskListSerializer
from .permission import IsStudent, IsTeacherOrAdmin
from learning_system.practice.models import PracticeCategory, PracticeTask


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



class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentMoveSerializer
    queryset = Student.objects
    permission_classes = [IsTeacherOrAdmin]

    '''
    @action(detail=True, methods=['POST', 'GET'])
    def move_to_group(self, request, pk=None):
        student = self.get_object()
        serializer = StudentMoveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #student = serializer.save()
            return Response({'status': 'student added'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    '''
    
class SetGroupView(generics.CreateAPIView):
    serializer_class = SetStudentGroupSerializer  
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

