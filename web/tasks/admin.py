from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskItemAdmin(admin.ModelAdmin):
    pass