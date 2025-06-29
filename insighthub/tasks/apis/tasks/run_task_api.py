
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from drf_spectacular.utils import extend_schema
from celery import signature

from insighthub.tasks.apis.tasks.serializers.serializers import InputTaskSerializer
from insighthub.tasks.constants import TASK_TAGS
from insighthub.tasks.models import Task
from celery import current_app

from insighthub.tasks.selectors.task_selectors import get_task_by_id, get_task_by_name
from insighthub.tasks.services.task_services import get_inputs
from insighthub.utils.convert_value_type import convert_value_type


class RunTaskByIdApi(APIView):
    @extend_schema(tags=TASK_TAGS, request=InputTaskSerializer,responses={200})
    def post(self, request, task_id):
        try:

            task = get_task_by_id(task_id=task_id)
            celery_task = current_app.tasks.get(task.name)
            serializer= InputTaskSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            args= get_inputs(task,serializer.validated_data.get("taskInput"))
            celery_task.delay(*args)
            return Response({"detail":"task ran successfully!"})
        except Exception as e:
            raise ValidationError(f"can not run task: {e}")


class RunTaskByNameApi(APIView):
    @extend_schema(tags=TASK_TAGS, request=InputTaskSerializer, responses={200})
    def post(self, request, task_name):
        try:

            task = get_task_by_name(task_name=task_name)
            celery_task = current_app.tasks.get(task.name)
            serializer = InputTaskSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            args = get_inputs(task, serializer.validated_data.get("taskInput"))
            celery_task.delay(*args)
            return Response({"detail": "task ran successfully!"})
        except Exception as e:
            raise ValidationError(f"can not run task: {e}")

class RunTaskBySignatureApi(APIView):
    @extend_schema(tags=TASK_TAGS, request=InputTaskSerializer, responses={200})
    def post(self,request, task_name):
        task = get_task_by_name(task_name=task_name)
        serializer = InputTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        args = get_inputs(task, serializer.validated_data.get("taskInput"))
        task_sig=signature(task_name,args)

        task_sig.apply_async()

        return Response({"detail":"task ran successfully"})