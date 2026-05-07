from app.tasks.celery_app import celery_app

@celery_app.task
def refresh_feeds():
    # Заглушка: просто логируем, БД пока не трогаем
    print("[Celery] refresh_feeds called (mock)")
    return {"status": "ok", "message": "Mock parser, no data saved"}