from rest_framework import serializers

from insighthub.api.serializer import AbstractListOutputSwaggerSerializer, SwaggerSerializer
from insighthub.users.apis.users.serializers.serializers import UserListCreateSerializer, UserOutputSerializer


class UserSwaggerOutPutSerializer(SwaggerSerializer):
    """User swagger input serializer"""
    result = UserOutputSerializer()


class UserListSwaggerSerializer(AbstractListOutputSwaggerSerializer):
    results = serializers.ListField(child=UserSwaggerOutPutSerializer())