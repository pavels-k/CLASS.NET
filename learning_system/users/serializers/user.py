from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from learning_system.users.models import StudyGroup, UserComplaint
from dry_rest_permissions.generics import DRYPermissionsField

UserModel = get_user_model()

#1
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

    username = serializers.CharField(label='Логин')
    password = serializers.CharField(label='Пароль',
                                     write_only=True,
                                     style={'input_type': 'password'})

    def validate(self, data):
        user = authenticate(username=data['username'],
                            password=data['password'])
        if not user:
            raise serializers.ValidationError(
                'There was typing wrong login or password')
        return data

#2
class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label='Логин')
    first_name = serializers.CharField(label='Имя')
    last_name = serializers.CharField(label='Фамилия')
    password = serializers.CharField(label='Пароль',
                                     min_length=6,
                                     write_only=True,
                                     style={'input_type': 'password'})
    password_confirmation = serializers.CharField(
        label='Подтверждение пароля',
        min_length=6,
        write_only=True,
        style={'input_type': 'password'})

    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name', 'username', 'password',
                  'password_confirmation')

    def validate(self, data):
        if data['password'] != data.pop('password_confirmation'):
            raise serializers.ValidationError("Passwords do not match!")
        return data

#11
class UserComplaintCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComplaint
        fields = ('user', 'complaints')

#12
class UserComplaintSerializer(UserComplaintCreateSerializer):
    user = UserCreateSerializer()



#20
class AddCourseToStudyGroup(serializers.ModelSerializer):
    name = serializers.CharField(label='Name of Group', read_only=True)
    class Meta:
        model = StudyGroup
        fields = ['available_subjects', 'name']
    '''
    def create(self, validated_data):
        pk = validated_data['id']
        study_group = StudyGroup.objects.get(pk=pk)
        course = validated_data['available_subjects']
        study_group.available_subjects.set(course)
        study_group.save()
        return study_group
    '''