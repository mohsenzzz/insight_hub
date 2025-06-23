from rest_framework import serializers

from insighthub.api.serializer import SwaggerSerializer, AbstractListOutputSwaggerSerializer
from insighthub.tasks.apis.tasks.serializers.serializers import TaskListCreateOutPutSerializer





class TaskSwaggerOutPutSerializer(SwaggerSerializer):
    """User swagger input serializer"""
    result = TaskListCreateOutPutSerializer()


class TaskListSwaggerSerializer(AbstractListOutputSwaggerSerializer):
    results = serializers.ListField(child=TaskSwaggerOutPutSerializer())