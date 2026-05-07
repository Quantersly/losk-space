from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str          # синхронная (psycopg2) для Alembic/скриптов
    ASYNC_DATABASE_URL: str    # асинхронная (asyncpg) для приложения
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    class Config:
        env_file = ".env"

settings = Settings()