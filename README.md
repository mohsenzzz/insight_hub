# InsightHub

## project setup

1- install dependencies
```
pip install requirements.txt
```
2- create your env
```
cp .env.example .env
```

3- run dependencies on docker 
```
sudo docker compose -f docker-compose.dev.yml up -d
```

4- Create tables
```
python manage.py migrate
```
5- initial project
```
python manage.py taskinit
```
6- create superuser
```
python manage.py createsuperuser
```
7- run server
```
python manage.py runserver
```
8- run celery
```
 celery -A config worker --loglevel=info

```
9- run celery beat
```
 celery -A config beat --loglevel=info -S django

```







