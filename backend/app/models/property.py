from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from geoalchemy2 import Geometry
from app.database import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    developer_id = Column(Integer, ForeignKey("developers.id"), nullable=False)

    # Стабильный идентификатор
    building = Column(String, nullable=False)
    floor = Column(Integer, nullable=False)
    apartment_number = Column(String, nullable=False)
    area = Column(Float, nullable=False)  # м²

    # Характеристики
    rooms = Column(Integer)
    price = Column(Float)
    address = Column(String)
    location = Column(Geometry('POINT', srid=4326))  # PostGIS
    status = Column(String, default="on_sale")  # on_sale / sold
    raw_data = Column(JSONB)  # оригинал из фида

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('building', 'floor', 'apartment_number', 'area',
                         name='uq_property_attributes'),
    )