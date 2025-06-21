from django.urls import path

from insighthub.users.apis.users.user_list_create_apis import UserListCreateApi
from insighthub.users.apis.users.user_retreive_update_delete_apis import UserRetrieveUpdateDeleteApi

app_name="users"

urlpatterns = [
    path('', UserListCreateApi.as_view(), name="user_list_create"),
    path('<int:user_id>/', UserRetrieveUpdateDeleteApi.as_view(), name="user_retrieve_update_delete")
]
