from django.contrib import admin
from users.models import * # NOQA F403
from labels.models import * # NOQA F403
from tasks.models import * # NOQA F403
from statuses.models import * # NOQA F403
# Register your models here.

admin.site.register(CustomUsers)
admin.site.register(Status)
admin.site.register(Label)
admin.site.register(Task)
