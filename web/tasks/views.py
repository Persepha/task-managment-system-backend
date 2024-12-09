from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import Task
from tasks.permissions import IsOwner
from tasks.selectors import task_list, task_list_by_user
from tasks.serializers import (
    FilterSerializer,
    TaskInputSerializer,
    TaskOutputSerializer,
    TaskUpdateInputSerializer,
)
from tasks.services import task_create, task_delete, task_update


class TaskListApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        filters_serializer = FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        user = self.request.user
        tasks = task_list_by_user(filters=filters_serializer.validated_data, user=user)

        data = TaskOutputSerializer(tasks, many=True).data

        return Response(data)


@extend_schema(request=TaskInputSerializer)
class TaskCreateApi(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = TaskInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.request.user

        created_task = task_create(**serializer.validated_data, user=user)

        return Response(status=status.HTTP_201_CREATED)


class TaskDeleteApi(APIView):
    permission_classes = (IsOwner | IsAdminUser,)

    def delete(self, request, id):
        task = get_object_or_404(Task, id=id)

        self.check_object_permissions(request, task)

        task_delete(task=task)

        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(request=TaskUpdateInputSerializer)
class TaskUpdateApi(APIView):
    permission_classes = (IsOwner | IsAdminUser,)

    def post(self, request, id):
        serializer = TaskUpdateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task = get_object_or_404(Task, id=id)

        self.check_object_permissions(request, task)

        updated_task, _ = task_update(task=task, data=serializer.validated_data)

        return Response(status=status.HTTP_200_OK)


class TaskDetailApi(APIView):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        serializer = TaskOutputSerializer(task)

        return Response(serializer.data)
