
from rest_framework import serializers

from insighthub.users.models import User


class UserListCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False)
    confirm_password = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","password","confirm_password")

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        if password and confirm_password is not None:
            if password != confirm_password:
                raise serializers.ValidationError("password don't match")
        return attrs

class UserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","first_name","last_name","username",'email')

class UserPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")

class UserPatchSerializer(serializers.Serializer):
    first_name= serializers.CharField(required=False)
    last_name= serializers.CharField(required=False)
    username= serializers.CharField(required=False)
    email= serializers.CharField(required=False)