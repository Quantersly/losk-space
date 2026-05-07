from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

sync_engine = create_engine(settings.DATABASE_URL, pool_size=10, max_overflow=20)
SyncSessionLocal = sessionmaker(bind=sync_engine)