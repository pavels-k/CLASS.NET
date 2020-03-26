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
