from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.shortcuts import (get_object_or_404, redirect, render,
                              render_to_response)
from django.urls import reverse

from learning_system.practice.serializers import PracticeTaskSerializer
from learning_system.users.models import Student, Teacher, StudyGroup, StudentProgress, UserComplaint, ReviewsOnTeacher
from learning_system.courses.models import Course
from learning_system.practice.models import PracticeCategory, PracticeTask
from learning_system.courses.serializers import CourseCreateSerializer
UserModel = get_user_model()


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

    username = serializers.CharField(label='Логин')
    password = serializers.CharField(label='Пароль', write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('There was typing wrong login or password')
        return data


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label='Логин')
    password = serializers.CharField(label='Пароль', min_length=6, write_only=True, style={'input_type': 'password'})
    password_confirmation = serializers.CharField(label='Подтверждение пароля', min_length=6, write_only=True,
                                                  style={'input_type': 'password'})

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'password_confirmation')

    def validate(self, data):
        if data['password'] != data.pop('password_confirmation'):
            raise serializers.ValidationError("Passwords do not match!")
        return data


class StudentCreateSerializer(UserCreateSerializer):
    class Meta:
        model = Student
        fields = ('id', 'username', 'password', 'password_confirmation')

    def create(self, validated_data):
        student = Student.objects.create(
            username=validated_data['username']
        )
        student.set_password(validated_data['password'])
        student.save()
        return student


class StudyGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = ('id', 'name', 'available_subjects')


class StudentSerializer(StudentCreateSerializer):
    study_group = StudyGroupCreateSerializer()
    class Meta:
       model = Student
       fields = ('id', 'username', 'password', 'password_confirmation', 'study_group')

class TeacherCreateSerializer(UserCreateSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'username', 'password', 'password_confirmation', 'study_groups')

    def create(self, validated_data):
        teacher = Teacher.objects.create(
            username=validated_data['username'],
        )
        groups = validated_data['study_groups']
        teacher.set_password(validated_data['password'])
        for group in groups:
            teacher.study_groups.add(group)
        teacher.save()
        return teacher


class StudentProgressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProgress
        fields = ('student', 'score', 'answers', 'practice_task')


class StudentProgressSerializer(StudentProgressCreateSerializer):
    student = StudentCreateSerializer()
    practice_task = PracticeTaskSerializer()


class UserComplaintCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComplaint
        fields = ('user', 'complaints')


class UserComplaintSerializer(UserComplaintCreateSerializer):
    user = UserCreateSerializer()


class ReviewsOnTeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewsOnTeacher
        fields = ('student', 'reviews', 'fullname')


class ReviewsOnTeacherSerializer(ReviewsOnTeacherCreateSerializer):
    student = StudentCreateSerializer()


class StudentMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'study_group')

class SetStudentGroupSerializer(serializers.ModelSerializer):
    #choices = Student.objects.values_list('pk', flat=True)
    #id = serializers.ChoiceField(label='ID студента', choices=choices)
    username = serializers.CharField(label='username', read_only=True)
    class Meta:
        model = Student
        fields = ( 'study_group', 'username')
    
    def create(self, validated_data):
        pk = validated_data['id']
        student = Student.objects.get(pk=pk)
        group = validated_data['study_group']
        student.study_group = group
        student.save()
        return student
    

class GetTaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeTask
        fields = ('__all__')
        

class ResultSerializer(serializers.ModelSerializer):
    student = StudentCreateSerializer()
    class Meta:
        model = StudentProgress
        fields = [ 'student', 'score', 'answers', 'practice_task']
        extra_kwargs = {
                'score': {
                    'required': False,
                 },
                 'answers': {
                    'required': False,
                 },
                 'practice_task': {
                    'required': False,
                 }
        }
    '''
    def create(self, validated_data):
        student = validated_data['student']
        student_progress = get_object_or_404(StudentProgress, student = student)
        student_progress.save()
        return student_progress
    '''



class StudentSelectSerializer(serializers.ModelSerializer):
    choices = Student.objects.values_list('study_group', flat=True)
    study_group = serializers.ChoiceField(label='ID группы', choices=choices)
    class Meta:
        model = Student
        fields = ['study_group',]



class AddCourseToStudyGroup(serializers.ModelSerializer):
    #choices = StudyGroup.objects.values_list('pk', flat=True)
    #id = serializers.ChoiceField(label='ID Группы', choices=choices)
    name = serializers.CharField(label='Name of Group', read_only=True)
    class Meta:
        model = StudyGroup
        fields = ['available_subjects', 'name']
    
    def create(self, validated_data):
        pk = validated_data['id']
        study_group = StudyGroup.objects.get(pk=pk)
        course = validated_data['available_subjects']
        study_group.available_subjects.set(course)
        study_group.save()
        return study_group

class StudyGroupSelectionSerializer(serializers.ModelSerializer):
    #available_subjects = CourseCreateSerializer(many=True)
    choices = Course.objects.values_list('pk', flat=True)
    available_subjects = serializers.ChoiceField(label='ID Группы', choices=choices)
    class Meta:
        model = StudyGroup
        fields = ['available_subjects',]

class CourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProgress
        exclude = ()

class ProgressSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()
    def get_progress(self,obj):
        course = self.context.get("course")
        #print(course)
        if course:
            practice_category = PracticeCategory.objects.filter(course = course)
            #print(practice_category[0])
            practice_tasks = PracticeTask.objects.filter(category = practice_category[0])
            #print(practice_tasks)
            student_progress = StudentProgress.objects.none()
            for practice_task in practice_tasks:
                student_progress |= StudentProgress.objects.filter(practice_task = practice_task)
            #student_progress = StudentProgress.objects.filter(practice_task = practice_task)
            print(student_progress)
            return CourseProgressSerializer(student_progress, many = True).data
        return None

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'progress')
        #fields = ('first_name', 'last_name',)
    
    
    '''
    study_group = StudyGroupSelectionSerializer()
    class Meta:
        model = Student
        fields = ['student', 'study_group']
    '''

