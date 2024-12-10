from rest_framework import serializers


class UserOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    is_staff = serializers.BooleanField()
    email = serializers.EmailField()


class TaskOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    closing_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")

    status = serializers.CharField(source="get_status_display", read_only=True)
    priority = serializers.CharField(source="get_priority_display", read_only=True)

    user = UserOutputSerializer(read_only=True)


class TaskInputSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    status = serializers.CharField(required=False)
    priority = serializers.CharField(required=False)
    closing_date =serializers.DateTimeField(required=False)


class TaskUpdateInputSerializer(TaskInputSerializer):
    title = serializers.CharField(required=False)


class FilterSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False, max_length=255)
    status = serializers.CharField(required=False, max_length=20)
    priority = serializers.CharField(required=False, max_length=20)
