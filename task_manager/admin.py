from django.contrib import admin
from users.models import CustomUsers
from labels.models import Label
from tasks.models import Task
from statuses.models import Status
# Register your models here.

admin.site.register(CustomUsers)
admin.site.register(Status)
admin.site.register(Label)
admin.site.register(Task)
