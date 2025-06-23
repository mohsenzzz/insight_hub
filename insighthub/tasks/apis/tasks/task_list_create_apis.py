from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from rest_framework import status

from insighthub.api.mixins import ApiAuthMixin
from insighthub.api.pagination import get_paginated_response_context, LimitOffsetPagination
from insighthub.tasks.apis.tasks.serializers.serializers import TaskListCreateOutPutSerializer, \
    TaskListCreateInputSerializer
from insighthub.tasks.apis.tasks.serializers.swagger_serializers import TaskListSwaggerSerializer, \
    TaskSwaggerOutPutSerializer
from insighthub.tasks.constants import TASK_TAGS
from insighthub.tasks.interfaces.task_interface import TaskCreatePutInterface, TaskInputInterface
from insighthub.tasks.selectors.task_selectors import get_unschedule_tasks
from insighthub.tasks.services.task_services import create_task


class TaskListCreateApi(ApiAuthMixin, APIView):

    @extend_schema(tags=TASK_TAGS, responses=TaskListSwaggerSerializer)
    def get(self, request):
        tasks = get_unschedule_tasks()

        return get_paginated_response_context(
            pagination_class=LimitOffsetPagination,
            serializer_class=TaskListCreateOutPutSerializer,
            queryset=tasks,
            request=request,
            view=self
        )

    @extend_schema(tags=TASK_TAGS, request=TaskListCreateInputSerializer, responses=TaskSwaggerOutPutSerializer)
    def post(self, request):
        serializer =TaskListCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print("===================================================")
        # print(serializer.validated_data)
        task_input_interface = [TaskInputInterface(
            name= input_task['name'],
            type= input_task["type"],
        ) for input_task in serializer.validated_data.get("taskInput")]
        task_interface = TaskCreatePutInterface(
                                    name= serializer.validated_data.get("name"),
                                    description=serializer.validated_data.get("description"),
                                    taskInput= task_input_interface

        )
        #

        task = create_task(task_interface)
        # return Response({'details': 'ok'}, status.HTTP_201_CREATED)

        #
        #
        return Response(TaskListCreateOutPutSerializer(instance=task).data, status=status.HTTP_201_CREATED)

