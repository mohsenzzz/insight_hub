from rest_framework import serializers

from insighthub.api.serializer import AbstractListOutputSwaggerSerializer, SwaggerSerializer
from insighthub.users.apis.users.serializers.serializers import UserListCreateSerializer


class UserSwaggerOutPutSerializer(SwaggerSerializer):
    """User swagger input serializer"""
    result = UserListCreateSerializer()


class UserListSwaggerSerializer(AbstractListOutputSwaggerSerializer):
    results = serializers.ListField(child=UserSwaggerOutPutSerializer())