from django.urls import path

from tasks.views import (
    TaskCreateApi,
    TaskDeleteApi,
    TaskDetailApi,
    TaskListApi,
    TaskUpdateApi,
)

urlpatterns = [
    path("", TaskListApi.as_view(), name="task-list"),
    path("create/", TaskCreateApi.as_view(), name="task-create"),
    path("<int:id>/", TaskDetailApi.as_view(), name="tak-detail"),
    path("<int:id>/delete/", TaskDeleteApi.as_view(), name="task-delete"),
    path("<int:id>/update/", TaskUpdateApi.as_view(), name="task-update"),
]
