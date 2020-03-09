from rest_framework import serializers

from .models import Course


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title')
