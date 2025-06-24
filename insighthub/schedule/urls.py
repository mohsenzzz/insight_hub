from django.urls import path

from insighthub.schedule.apis.schedules.schedule_list_create_apis import ScheduleListCreateApi
from insighthub.schedule.apis.schedules.schedule_retrieve_update_delete_apis import ScheduleRetrieveUpdateDestroy

app_name="schedule"
urlpatterns =[
    path('',ScheduleListCreateApi.as_view(), name="schedule_list_create"),
    path('<int:schedule_id>/',ScheduleRetrieveUpdateDestroy.as_view(), name="schedule_retrieve_update_destroy")
]