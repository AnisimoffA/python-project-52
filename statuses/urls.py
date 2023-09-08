from statuses.views import * # NOQA F403
from django.urls import path


urlpatterns = [
    path('', StatusesList.as_view(), name="statuses_list"),
    path('create/', StatusesCreate.as_view(), name="statuses_create"),
    path('<int:pk>/update/', StatusesUpdate.as_view(), name="statuses_update"),
    path('<int:pk>/delete/', StatusesDelete.as_view(), name="statuses_delete"),
]
