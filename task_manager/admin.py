from django.contrib import admin
from task_manager.users.models import CustomUsers
from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
# Register your models here.

admin.site.register(CustomUsers)
admin.site.register(Status)
admin.site.register(Label)
admin.site.register(Task)
