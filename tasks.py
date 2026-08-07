from celery import Celery
from asgiref.sync import async_to_sync
import os
from celery.schedules import crontab

redis_url = os.getenv('REDIS_URL')
c_app = Celery(broker=redis_url or "redis://localhost:6379/1", backend=redis_url, imports=['PersonalNews.tasks'])
# c_app.autodiscover_tasks(['PersonalNews'])

@c_app.task(name="send_periodic_email")
def send_email(message: str):
	from PersonalNews.routers.users import send_message
	async_to_sync(send_message)(message)

c_app.conf.beat_schedule = {
	"run-every-minute": {
		"task": "send_periodic_email",
		"schedule": crontab(minute="*"),
		"args": ("Привет из Celery Beat!",)
	}
}