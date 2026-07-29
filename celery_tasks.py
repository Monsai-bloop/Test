from celery import Celery
from asgiref.sync import async_to_sync
import os

redis_url = os.getenv('REDIS_URL')
c_app = Celery(broker=redis_url, backend=redis_url)
c_app.autodiscover_tasks(['PersonalNews'])

@c_app.task()
def send_email(message: str):
	from PersonalNews.routers.users import send_message
	async_to_sync(send_message)(message)