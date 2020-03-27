from rest_framework import viewsets
from dry_rest_permissions.generics import DRYPermissions

from learning_system.courses.models import Course
from learning_system.courses.serializers import CourseCreateSerializer


class CourseView(viewsets.ModelViewSet):
    permission_classes = (DRYPermissions,)
    serializer_class = CourseCreateSerializer
    queryset = Course.objects.all()
