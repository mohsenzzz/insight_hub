import os
import requests
from datetime import datetime

from celery import shared_task
import pandas as pd

from config.env import env
from config.django.base import MEDIA_ROOT
from insighthub.users.selectors.user_selectors import get_all_users


@shared_task
def get_user_report(file_name: str):
    users = get_all_users()
    users_data = list(users.values("first_name","last_name","username","email"))
    df = pd.DataFrame(users_data)
    name, ext = os.path.splitext(file_name)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name = f"{name}_{timestamp}{ext}"
    file_path= os.path.join(MEDIA_ROOT, 'reports', file_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_excel(file_path)
    return file_path


@shared_task
def get_usd_value():
    url = env("USD_URL")
    response = requests.get(url, timeout=10)
    print(response)
    data = [value for key, value in response.items()]
    df = pd.DataFrame(data)
    file_name = "usd.xlsx"
    file_path = os.path.join(MEDIA_ROOT, 'usd', file_name)
    if os.path.exists(file_path):
        existing_data = pd.read_excel(file_path)
        combined_data = pd.concat([existing_data, df], ignore_index=True)
        combined_data.to_excel(file_path, index=False)
    else:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df.to_excel(file_path)