from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from learning_system.users.serializers import GroupDetailSerializer
from learning_system.users.models import User
from learning_system.users.serializers import UserSerializer, PasswordSerializer,StudentSerializer



class GroupCreateView(generics.CreateAPIView):
    serializer_class = GroupDetailSerializer


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def recent_users(self, request):
        recent_users = User.objects.all().order_by('-last_login')

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    @action(detail=True, methods=['POST','GET'])
    def move_to_group(self, request, pk=None):
           student = self.get_object()
           serializer = StudentSerializer(data=request.data)
           if serializer.is_valid():
                 serializer.save()
                 return Response({'status': 'student added'})
           else:
                return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)