from rest_framework import serializers

from learning_system.courses.models import Course


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title')
        
