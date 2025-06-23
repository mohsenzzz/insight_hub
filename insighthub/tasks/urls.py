
from django.urls import path

from insighthub.tasks.apis.tasks.task_list_create_apis import TaskListCreateApi

app_name="tasks"
urlpatterns=[
    path('', TaskListCreateApi.as_view(), name="task_list_create")
]