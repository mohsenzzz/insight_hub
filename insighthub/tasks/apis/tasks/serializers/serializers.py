
from rest_framework import serializers

from insighthub.tasks.models import Task, TaskInput
from insighthub.users.apis.users.serializers.serializers import UserOutputSerializer

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id","name","description")

class TaskInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskInput
        fields = ( "name","type")


class TaskListCreateInputSerializer(serializers.ModelSerializer):
    taskInput = TaskInputSerializer(many=True)
    class Meta:
        model=Task
        fields=("name", "description","taskInput")



class TaskListCreateOutPutSerializer(serializers.ModelSerializer):
    taskInput = serializers.SerializerMethodField()
    class Meta:
        model=Task
        fields=("id","name", "description","taskInput")

    def get_taskInput(self,obj):
        task_input = obj.task_inputs.all()
        return TaskInputSerializer(instance=task_input, many=True).data

class InputTaskSerializer(serializers.Serializer):
    taskInput= serializers.JSONField(required=False)