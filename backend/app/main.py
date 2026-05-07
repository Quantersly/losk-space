from fastapi import FastAPI
from app.api.v1 import properties

app = FastAPI(title="Losk Space API", version="0.1.0")
app.include_router(properties.router, prefix="/api/v1/properties", tags=["properties"])
