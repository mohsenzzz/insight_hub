from rest_framework import serializers

from insighthub.api.serializer import SwaggerSerializer, AbstractListOutputSwaggerSerializer
from insighthub.schedule.apis.schedules.serializers.serialziers import ScheduleListCreateSerializer


class ScheduleSwaggerOutPutSerializer(SwaggerSerializer):
    """User swagger input serializer"""
    result = ScheduleListCreateSerializer()


class ScheduleListSwaggerSerializer(AbstractListOutputSwaggerSerializer):
    results = serializers.ListField(child=ScheduleSwaggerOutPutSerializer())