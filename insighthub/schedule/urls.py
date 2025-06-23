from django.urls import path

from insighthub.schedule.apis.schedules.schedule_list_create_apis import ScheduleListCreateApi


app_name="schedule"
urlpatterns =[
    path('',ScheduleListCreateApi.as_view(), name="schedule_list_create")
]