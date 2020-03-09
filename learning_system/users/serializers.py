from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

from learning_system.practice.serializers import PracticeTaskSerializer
from .models import Student, Teacher, StudyGroup, StudentProgress, UserComplaint, ReviewsOnTeacher
from learning_system.courses.models import Course
from learning_system.practice.models import PracticeCategory, PracticeTask
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
        #fields = ('id', 'username', 'password', 'password_confirmation', 'study_group')
        fields = ('id', 'username', 'password', 'password_confirmation')

    def create(self, validated_data):
        student = Student.objects.create(
            username=validated_data['username']
            #study_group=validated_data['study_group']
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
    choices = Student.objects.values_list('pk', flat=True)
    id = serializers.ChoiceField(label='ID студента', choices=choices)

    class Meta:
        model = Student
        fields = ('id', 'study_group')
    
    def create(self, validated_data):
        pk = validated_data['id']
        student = Student.objects.get(pk=pk)
        group = validated_data['study_group']
        student.study_group = group
        student.save()
        return student
    

class CourseSerializer(serializers.Serializer):
    choices = Course.objects.values_list('title', flat=True)
    course = serializers.ChoiceField(label='Курс', choices=choices)
    class Meta:
        model = Course
        fields = ('title')

class StudyGroupSerializer(serializers.Serializer):
    available_subjects = CourseSerializer()
    class Meta:
        model = Course
        fields = ('available_subjects')

class GetTaskListSerializer(serializers.Serializer):
    '''
    choices = Course.objects.values_list('title', flat=True)
    #choices = StudyGroup.available_subjects('title', flat=True)
    course = serializers.ChoiceField(label='Курс', choices=choices)
    '''
    study_group = StudyGroupSerializer()
    class Meta:
        model = Student
        fields = ('study_group',)
    
    def create(self, validated_data):
        #course_pk = validated_data['id']
        #course = Course.objects.get(pk=course_pk)
        
        '''
        if course in study_group.available_subjects.all():
            practice_category = PracticeCategory.objects.get(course=course)
            task_list = PracticeTask.objects.filter(practice_category=practice_category)
            return task_list
        '''
        return PracticeTask.objects.none()
        #return PracticeTask.objects.all()
    
    def update(self, instance, validated_data):
        print('ssss\n')
        print(validated_data)
        print(validated_data)
        print(validated_data)
        print('ssss\n')
        '''
        student = Student.objects.get(id = instance.id)
        study_group = student.study_group
        course = validated_data.course
        #instance.complexity = validated_data.get('complexity', instance.complexity)
        if course in study_group.available_subjects.all():
            practice_category = PracticeCategory.objects.get(course=course)
            task_list = PracticeTask.objects.filter(practice_category=practice_category)
            return task_list
        '''
        return PracticeTask.objects.none()
