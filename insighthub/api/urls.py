from django.urls import path, include

urlpatterns = [
    # path('blog/', include(('insighthub.blog.urls', 'blog')))
    path('users/', include(('insighthub.users.urls', 'users'))),
    path('auth/', include(('insighthub.authentication.urls', 'auth'))),
    path('tasks/', include(('insighthub.tasks.urls', 'tasks'))),
    path('schedules/', include(('insighthub.schedule.urls', 'schedule'))),
]
