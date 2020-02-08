from django.shortcuts import render
from rest_framework import generics
from learning_system.users.serializers import UserDetailSerializer

# Create your views here.
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer