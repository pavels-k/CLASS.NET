from rest_framework import serializers

from learning_system.courses.serializers import CourseCreateSerializer
from learning_system.practice.models import PracticeCategory, AbstractTask
from learning_system.users.models import StudyGroup, Student
from learning_system.courses.models import Course

class PracticeCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeCategory
        fields = ('parent', 'course')


class PracticeCategorySerializer(PracticeCategoryCreateSerializer):
    course = CourseCreateSerializer()


class PracticeTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractTask
        fields = ('content', 'complexity', 'task_type', 'category')


class PracticeTaskSerializer(serializers.ModelSerializer):
    #category = PracticeCategorySerializer()
    class Meta:
        model = AbstractTask
        fields = ('content', 'complexity', 'task_type')
    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.complexity = validated_data.get('complexity', instance.complexity)
        instance.task_type = validated_data.get('task_type', instance.task_type)
        instance.save()
        return instance
'''
class TaskUserDataCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskUserData
        fields = ('practice_task', 'status', 'tries_count', 'user_answer', 'correct_answer')

class TaskUserDataSerializer(TaskUserDataCreateSerializer):
    practice_task = PracticeTaskSerializer()
'''

    