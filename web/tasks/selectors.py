from django.db.models import QuerySet
from django.conf import settings

from tasks.filters import BaseTaskFilter
from tasks.models import Task


def task_list(*, filters=None) -> QuerySet[Task]:
    filters = filters or {}

    qs = Task.objects.all().select_related("user")

    return BaseTaskFilter(filters, qs).qs


def task_list_by_user(*, filters=None, user: settings.AUTH_USER_MODEL) -> QuerySet[Task]:
    filters = filters or {}

    qs = Task.objects.select_related("user").filter(user=user)

    return BaseTaskFilter(filters, qs).qs