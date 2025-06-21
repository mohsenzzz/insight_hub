from django.urls import path

from insighthub.users.apis.users.user_apis import UserListCreateApi

app_name="users"

urlpatterns = [
    path('', UserListCreateApi.as_view(), name="user_list_create")
]
