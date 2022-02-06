from django.contrib import admin

# Register your models here.
from SoftUni_Web.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
