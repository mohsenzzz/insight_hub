from rest_framework import serializers


class SwaggerSerializer(serializers.Serializer):
    result = serializers.JSONField()
    status = serializers.IntegerField()
    success = serializers.BooleanField()
    messages = serializers.ListField()


class AbstractListOutputSwaggerSerializer(serializers.Serializer):
    count = serializers.IntegerField(help_text="Total number of items.")
    next = serializers.CharField(allow_null=True, help_text="URL to the next page of results.", required=False)
    previous = serializers.CharField(allow_null=True, help_text="URL to the previous page of results.", required=False)
    page_size = serializers.IntegerField(help_text="Number of items per page.")
    results = serializers.ListField(child=serializers.DictField(), help_text="List of objects.")
    page = serializers.IntegerField(required=False, help_text='number of page')


class PaginationFilterSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False)
    page_size= serializers.IntegerField(required=False)