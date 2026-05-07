from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.property import Property

router = APIRouter()

@router.get("/{property_id}")
async def get_property(property_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Property).where(Property.id == property_id))
    prop = result.scalar_one_or_none()
    if not prop:
        raise HTTPException(status_code=404, detail="Not found")
    return {
        "id": prop.id,
        "building": prop.building,
        "floor": prop.floor,
        "apartment_number": prop.apartment_number,
        "area": prop.area,
        "price": prop.price,
        "status": prop.status
    }


@router.get("/")
async def get_properties(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Property).limit(10).offset(0))
    props = result.scalars().all()
    if not props:
        raise HTTPException(status_code=500, detail="Internal Server Error ")
    return props