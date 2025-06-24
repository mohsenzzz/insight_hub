from config.env import env

# https://docs.celeryproject.org/en/stable/userguide/configuration.html

CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='amqp://guest:guest@localhost//')
CELERY_RESULT_BACKEND = 'django-db'

CELERY_TIMEZONE = 'Asia/Tehran'

CELERY_TASK_SOFT_TIME_LIMIT = 20  # seconds
CELERT_TASK_TIME_LIMIT = 30  # seconds
CELERY_TASK_MAX_RETRIES = 3

CELERY_BEAT_SCHEDULE = 'django_celery_beat.schedulers:DatabaseScheduler'