import os
from datetime import datetime

from celery import shared_task
import pandas as pd

from config.django.base import MEDIA_ROOT
from insighthub.users.selectors.user_selectors import get_all_users


@shared_task
def get_user_report(file_name: str):
    users = get_all_users()
    users_data = list(users.values("first_name","last_name","username","email"))
    df = pd.DataFrame(users_data)
    file_name = file_name + str(datetime.now())
    file_path= os.path.join(MEDIA_ROOT, 'reports', file_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_excel(file_path)
    return file_path
