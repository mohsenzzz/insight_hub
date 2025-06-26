
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status

from insighthub.api.mixins import ApiAuthMixin
from insighthub.api.pagination import get_paginated_response_context, LimitOffsetPagination
from insighthub.api.serializer import PaginationFilterSerializer
from insighthub.schedule.apis.schedules.serializers.serialziers import ScheduleCreateSerializer, \
    ScheduleOutputSerializer
from insighthub.schedule.apis.schedules.serializers.swagger_serializers import ScheduleSwaggerOutPutSerializer, \
    ScheduleListSwaggerSerializer
from insighthub.schedule.constants import SCHEDULE_TAGS
from insighthub.schedule.interfaces.schedule_interface import ScheduleInterface
from insighthub.schedule.selectors.schedule_selectors import get_User_schedules
from insighthub.schedule.services.celery_services import create_periodic_task
from insighthub.schedule.services.schedule_services import create_schedule
from insighthub.utils.pagination import CustomPaginationPagination


class ScheduleListCreateApi(ApiAuthMixin,APIView):

    @extend_schema(tags=SCHEDULE_TAGS, responses=ScheduleListSwaggerSerializer, parameters=[PaginationFilterSerializer])
    def get(self, request):
        schedules= get_User_schedules(user_id=request.user.id)

        return get_paginated_response_context(
            pagination_class=CustomPaginationPagination,
            serializer_class=ScheduleOutputSerializer,
            queryset=schedules,
            request=request,
            view=self
        )

    @extend_schema(tags=SCHEDULE_TAGS,request=ScheduleCreateSerializer, responses=ScheduleSwaggerOutPutSerializer)
    def post(self,request):

        serializer=ScheduleCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        schedule_interface=ScheduleInterface(
                    cron_expression=serializer.validated_data.get("cron_expression"),
                    enabled=serializer.validated_data.get("enabled"),
                    arguments=serializer.validated_data.get("arguments")
        )
        schedule = create_schedule(schedule_interface=schedule_interface,
                                   user=request.user,
                                   task_id=serializer.validated_data.get("task_id"),
                                   )
        #
        #

        create_periodic_task(schedule= schedule)


        return Response(ScheduleOutputSerializer(instance=schedule).data, status=status.HTTP_201_CREATED)