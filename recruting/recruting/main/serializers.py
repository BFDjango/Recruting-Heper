from rest_framework import serializers

from recruting.main.models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    role = serializers.IntegerField(required=True)
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'role')

