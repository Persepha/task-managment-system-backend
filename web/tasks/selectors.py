from django.db.models import QuerySet

from tasks.filters import BaseTaskFilter
from tasks.models import Task


def task_list(*, filters=None) -> QuerySet[Task]:
    filters = filters or {}

    qs = Task.objects.all().select_related("user")

    return BaseTaskFilter(filters, qs).qs
