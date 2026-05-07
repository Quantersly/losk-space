from celery import Celery
from app.config import settings

celery_app = Celery(
    "losk_space",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=["app.tasks.feed_parser_task"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,

    task_routes = {
        "app.tasks.feed_parser_task.*": {"queue": "parser_queue"},
        "app.tasks.user_tasks.*": {"queue": "user_queue"},
    },
)