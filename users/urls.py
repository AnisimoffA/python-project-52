from django.urls import path
from users.views import UserList, UserRegister, UserUpdate, UserDelete # NOQA E501


urlpatterns = [
    path('', UserList.as_view(), name="users_list"),
    path('create/', UserRegister.as_view(), name="users_register"),
    path('<int:pk>/update/', UserUpdate.as_view(), name="users_update"),
    path('<int:pk>/delete/', UserDelete.as_view(), name="users_delete"),
]
