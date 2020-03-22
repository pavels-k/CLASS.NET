from rest_framework import serializers
from learning_system.users.serializers.user import UserCreateSerializer
from learning_system.users.models import Teacher, Student, StudentProgress
from learning_system.users.serializers.student import StudentCreateSerializer


#7
class TeacherCreateSerializer(UserCreateSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'username', 'password',
                  'password_confirmation', 'study_groups')

    def create(self, validated_data):
        teacher = Teacher.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'])
        groups = validated_data['study_groups']
        teacher.set_password(validated_data['password'])
        for group in groups:
            teacher.study_groups.add(group)
        teacher.save()
        return teacher
#8
class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'username','study_groups')


#16
class SetStudentGroupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label='username', read_only=True)
    class Meta:
        model = Student
        fields = ('study_group', 'username')

    def create(self, validated_data):
        pk = validated_data['id']
        student = Student.objects.get(pk=pk)
        group = validated_data['study_group']
        student.study_group = group
        student.save()
        return student



#18
class ResultSerializer(serializers.ModelSerializer):
    student = StudentCreateSerializer() # исправить

    class Meta:
        model = StudentProgress
        fields = ['student', 'score', 'answers', 'practice_task']
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

#19
class StudentSelectSerializer(serializers.ModelSerializer):
    choices = Student.objects.values_list('study_group', flat=True)
    study_group = serializers.ChoiceField(label='ID группы', choices=choices)

    class Meta:
        model = Student
        fields = [
            'study_group',
        ]
