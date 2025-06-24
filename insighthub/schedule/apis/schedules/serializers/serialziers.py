
from croniter import croniter
from rest_framework import serializers

from insighthub.schedule.models import Schedule
from insighthub.tasks.apis.tasks.serializers.serializers import TaskSerializer
from insighthub.tasks.selectors.task_selectors import get_task_by_id
from insighthub.utils.validate_type_arguments import validate_argument_type


# class ScheduleListCreateSerializer(serializers.ModelSerializer):
#     task= TaskSerializer()
#     class Meta:
#         model= Schedule
#         fields = ("id", "cron_expression", "enabled","task")
#
#     def validate_cron_expression(self, value):
#         try:
#             croniter(value)
#         except Exception as e:
#             raise serializers.ValidationError(f"cron_expression is invalid: {e}")

class ScheduleCreateSerializer(serializers.ModelSerializer):
    task_id = serializers.IntegerField()
    arguments = serializers.JSONField()
    class Meta:
        model = Schedule
        fields=("cron_expression", "enabled","task_id", "arguments")

    def validate(self, attrs):
        #validate cron_expression
        try:
            croniter(attrs.get("cron_expression"))
        except Exception as e:
                raise serializers.ValidationError(f"cron_expression is invalid: {e}")

        #validate task_id
        task = get_task_by_id(task_id=attrs.get("task_id"))

        #validate argumenta
        task_inputs = task.task_inputs.all()
        arguments= attrs.get("arguments")
        for task_input in task_inputs:
               if not arguments.get(task_input.name):
                     raise serializers.ValidationError(f"there is not argument {task_input.name} for task {task.name}")
               validate_argument_type(filed_type=task_input.type, value=arguments.get(task_input.name))

        return attrs

class SchedulePatchSerializer(serializers.ModelSerializer):
    class Meta:
        model= Schedule
        fields = ("enabled", "arguments")

class ScheduleOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model=Schedule
        fields=("id","cron_expression", "enabled","task_id", "arguments")

