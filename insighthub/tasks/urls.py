
from django.urls import path

from insighthub.tasks.apis.tasks.run_task_api import RunTaskByIdApi, RunTaskByNameApi, RunTaskBySignatureApi
from insighthub.tasks.apis.tasks.task_list_create_apis import TaskListCreateApi

app_name="tasks"
urlpatterns=[
    path('', TaskListCreateApi.as_view(), name="task_list_create"),
    path('run/<int:task_id>', RunTaskByIdApi.as_view(), name="run_task_by_id"),
    path('run/<str:task_name>', RunTaskByNameApi.as_view(), name="run_task_by_name"),
    path('run/signature/<str:task_name>', RunTaskBySignatureApi.as_view(), name="run_task_by_signature"),
]