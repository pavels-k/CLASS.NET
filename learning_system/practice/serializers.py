from rest_framework import serializers

from learning_system.courses.serializers import CourseCreateSerializer
from learning_system.practice.models import PracticeCategory, PracticeTask, TaskUserData
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
        model = PracticeTask
        fields = ('content', 'complexity', 'task_type', 'category')


class PracticeTaskSerializer(serializers.ModelSerializer):
    #category = PracticeCategorySerializer()
    class Meta:
        model = PracticeTask
        fields = ('content', 'complexity', 'task_type')
    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.complexity = validated_data.get('complexity', instance.complexity)
        instance.task_type = validated_data.get('task_type', instance.task_type)
        instance.save()
        return instance

class TaskUserDataCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskUserData
        fields = ('practice_task', 'status', 'tries_count', 'user_answer', 'correct_answer')

class TaskUserDataSerializer(TaskUserDataCreateSerializer):
    practice_task = PracticeTaskSerializer()

class GetTaskListSerializer(serializers.Serializer):
    #course = CourseCreateSerializer()
    student_choices = Student.objects.values_list('pk', flat=True)
    student_id = serializers.ChoiceField(label='ID студента', choices=student_choices)
    course_choices = Course.objects.values_list('pk', flat=True)
    course_id = serializers.ChoiceField(label='ID курса', choices=course_choices)
    
    '''
    class Meta:
        #student_choices = Student.objects.values_list('pk', flat=True)
        #student_id = serializers.ChoiceField(label='ID студента', choices=student_choices)
        model = Student
        #fields = ('student_id',)
        #course_choices = Course.objects.values_list('pk', flat=True)
        #course_id = serializers.ChoiceField(label='ID курса', choices=course_choices)
        #course_choices = Course.objects.values_list('pk', flat=True)
        #course_id = serializers.ChoiceField(label='ID курса', choices=course_choices)
        #model = Course
        fields = ()
        read_only_fields = ('student_id', 'course_id')
    '''
    def create(self, validated_data):
        
        
        student_pk = validated_data['student_id']
        student = Student.objects.get(pk=student_pk)
        course_pk = validated_data['course_id']
        course = Course.objects.get(pk=course_pk)
        study_group = student.study_group
        
        if study_group and course in study_group.available_subjects.all():
            practice_category = PracticeCategory.objects.get(course=course)
            task_list = PracticeTask.objects.filter(practice_category=practice_category)
            return task_list
        
        #return PracticeTask.objects.none()
        return PracticeTask.objects.all()

    