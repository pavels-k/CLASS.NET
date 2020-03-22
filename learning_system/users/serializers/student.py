from rest_framework import serializers
from learning_system.users.serializers.user import UserCreateSerializer
from learning_system.users.models import Student, StudyGroup, StudentProgress, ReviewsOnTeacher
from learning_system.practice.models import PracticeTask
from learning_system.courses.serializers import CourseCreateSerializer
from learning_system.practice.serializers import PracticeTaskSerializer, PracticeCategory


#3
class StudentCreateSerializer(UserCreateSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'username', 'password',
                  'password_confirmation')

    def create(self, validated_data):
        student = Student.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'])
        student.set_password(validated_data['password'])
        student.save()
        return student


#4
class StudyGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = ('id', 'name', 'available_subjects')
#5
class StudyGroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = ('id', 'name', 'available_subjects')
#6
class StudentListSerializer(serializers.ModelSerializer):
    study_group = StudyGroupCreateSerializer()
    class Meta:
        model = Student
        fields = ('id', 'username', 'study_group')
#9
class StudentProgressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProgress
        fields = ('student', 'score', 'answers', 'practice_task')

#10
class StudentProgressSerializer(StudentProgressCreateSerializer):
    student = StudentCreateSerializer()
    practice_task = PracticeTaskSerializer()

#13
class ReviewsOnTeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewsOnTeacher
        fields = ('student', 'reviews', 'fullname')

#14
class ReviewsOnTeacherSerializer(ReviewsOnTeacherCreateSerializer):
    student = StudentCreateSerializer()
#17
class GetTaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeTask
        fields = ('__all__')

#22
class CourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProgress
        exclude = ()

#23
class ProgressSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()

    def get_progress(self, obj):
        course = self.context.get("course")
        if course:
            practice_category = PracticeCategory.objects.filter(course=course)
            practice_tasks = PracticeTask.objects.filter(
                category=practice_category[0])
            student_progress = StudentProgress.objects.none()
            for practice_task in practice_tasks:
                student_progress |= StudentProgress.objects.filter(
                    practice_task=practice_task)
            return CourseProgressSerializer(student_progress, many=True).data
        return None

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'progress')
