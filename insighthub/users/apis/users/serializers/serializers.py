
from rest_framework import serializers

from insighthub.users.models import User


class UserListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email")