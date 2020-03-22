from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from learning_system.users.permission import IsAdminUser
from learning_system.users.models import StudyGroup, UserComplaint
from learning_system.users.serializers.user import UserCreateSerializer , \
    UserLoginSerializer, \
    UserComplaintCreateSerializer, \
    UserComplaintSerializer, \
    AddCourseToStudyGroup


#3
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('users:login_user'))


#4
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
                    return Response('You are signed in successfully as %s' %
                                    user.username)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#5
class UserCreateView(viewsets.ModelViewSet):
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


#12
class UserComplaintCreateView(viewsets.ModelViewSet):
    serializer_class = UserComplaintCreateSerializer
    queryset = UserComplaint.objects.all()


#13
class UserComplaintView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserComplaintSerializer
    queryset = UserComplaint.objects.all()


#19
class AddCourseToStudyGroupView(viewsets.ModelViewSet):
    serializer_class = AddCourseToStudyGroup
    queryset = StudyGroup.objects.all()
    permission_classes = [IsAdminUser]