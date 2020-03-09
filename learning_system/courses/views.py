from rest_framework import generics

from learning_system.courses.models import Course
from .serializers import CourseCreateSerializer


class CourseCreateView(generics.CreateAPIView):
    serializer_class = CourseCreateSerializer


class CourseView(generics.ListAPIView):
    serializer_class = CourseCreateSerializer
    queryset = Course.objects
