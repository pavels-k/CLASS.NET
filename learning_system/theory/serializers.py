from rest_framework import serializers

from learning_system.courses.serializers import CourseCreateSerializer
from learning_system.theory.models import TheoryCategory, TheoryPost


class TheoryCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheoryCategory
        fields = ('parent', 'course')


class TheoryCategorySerializer(TheoryCategoryCreateSerializer):
    course = CourseCreateSerializer()


class TheoryPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheoryPost
        fields = ('content', 'category')


class TheoryPostSerializer(TheoryPostCreateSerializer):
    category = TheoryCategorySerializer()
