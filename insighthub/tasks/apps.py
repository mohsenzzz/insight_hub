from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'insighthub.tasks'

    def ready(self):
        import insighthub.tasks.tasks
