from datetime import date, datetime
from typing import Tuple

from django.conf import settings
from django.db import transaction

from common.exceptions import ApplicationError
from common.services import model_update
from tasks.models import Task


def task_create(
    *,
    title: str,
    priority: str = Task.LOW,
    status: str = Task.PENDING,
    description: str = "",
    user: settings.AUTH_USER_MODEL,
    closing_date: datetime | None = None
) -> Task:

    task = Task(
        title=title,
        description=description,
        priority=priority,
        user=user,
        status=status,
        closing_date=closing_date,
    )
    task.full_clean()
    task.save()

    return task


def task_delete(*, task: Task):
    task.delete()


@transaction.atomic
def task_update(*, task: Task, data) -> Tuple[Task, bool]:
    non_side_effect_fields = ["description", "title", "status", "priority"]

    task, has_updated = model_update(
        instance=task,
        fields=non_side_effect_fields,
        data=data,
    )

    return task, has_updated
