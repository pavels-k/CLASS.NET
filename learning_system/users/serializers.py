from rest_framework import serializers
from learning_system.users.models import Group, User
from django.contrib.auth import get_user_model


class GroupDetailSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Group
        fields = '__all__'


UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password","groups", )

class PasswordSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = User
        fields = ('password')

class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        student = UserModel.objects.create(
            username=validated_data['username']
        )
        student.set_password(validated_data['password'])
        student.save()
        return student