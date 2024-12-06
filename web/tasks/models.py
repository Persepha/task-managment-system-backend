from django.conf import settings
from django.db import models

from common.models import BaseModel


class Task(BaseModel):
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )

    description = models.TextField(blank=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    PENDING = "pending"
    IN_PROCESS = "in process"
    DONE = "done"
    TASK_STATUS_CHOICES = {
        PENDING: "Pending",
        IN_PROCESS: "In process",
        DONE: "Done",
    }

    status = models.CharField(
        max_length=20, choices=TASK_STATUS_CHOICES, default=PENDING
    )

    MEDIUM = "medium"
    HIGH = "high"
    LOW = "low"
    TASK_PRIORITY_CHOICES = {
        MEDIUM: "Medium",
        HIGH: "High",
        LOW: "Low",
    }

    priority = models.CharField(
        max_length=20, choices=TASK_PRIORITY_CHOICES, default=LOW
    )

    closing_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Task {self.id} - {self.title}"
