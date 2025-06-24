from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from insighthub.api.mixins import ApiAuthMixin
from insighthub.schedule.apis.schedules.serializers.serialziers import ScheduleOutputSerializer, \
    SchedulePatchSerializer
from insighthub.schedule.apis.schedules.serializers.swagger_serializers import ScheduleSwaggerOutPutSerializer
from insighthub.schedule.constants import SCHEDULE_TAGS
from insighthub.schedule.interfaces.schedule_interface import SchedulePatchInterface
from insighthub.schedule.selectors.schedule_selectors import get_schedule_by_id
from insighthub.schedule.services.schedule_services import partial_update_schedule, delete_schedule


class ScheduleRetrieveUpdateDestroy(ApiAuthMixin,APIView):
    @extend_schema(tags=SCHEDULE_TAGS, responses= ScheduleSwaggerOutPutSerializer)
    def get(self, request, schedule_id):
        schedule = get_schedule_by_id(schedule_id=schedule_id)

        return Response(ScheduleOutputSerializer(instance=schedule).data, status=status.HTTP_200_OK)

    @extend_schema(tags=SCHEDULE_TAGS,request=SchedulePatchSerializer, responses=ScheduleSwaggerOutPutSerializer)
    def patch(self, request, schedule_id):

        schedule = get_schedule_by_id(schedule_id=schedule_id)
        serializer = SchedulePatchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        schedule_interface =  SchedulePatchInterface(
                    enabled= serializer.validated_data.get("enabled",None),
                    arguments= serializer.validated_data.get("arguments", None)
        )
        schedule= partial_update_schedule(schedule_interface, schedule, request.user)


        return  Response(ScheduleOutputSerializer(instance=schedule).data, status=status.HTTP_200_OK)

    @extend_schema(tags=SCHEDULE_TAGS,  responses={204: "accepted"})
    def delete(self,request, schedule_id):
        schedule= get_schedule_by_id(schedule_id=schedule_id)
        delete_schedule(schedule)
        return Response(status=status.HTTP_204_NO_CONTENT)

