from rest_framework import serializers
from learning_system.users.models import Group, User


class UserDetailSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = User
        fields = '__all__'