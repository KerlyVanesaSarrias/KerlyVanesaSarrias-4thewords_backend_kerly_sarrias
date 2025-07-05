from datetime import date
from select import select
from typing import Optional
from fastapi import HTTPException, UploadFile
from sqlmodel import Session
from app.models.legend_model import Legend
from app.schemas.legend_schema import LegendCreate, LegendUpdate
from app.repositories import legend_repository
from uuid import UUID, uuid4
from typing import Optional, List
from sqlmodel import Session, select
from app.models.legend_model import Legend
from app.models.location_model import Location
from sqlalchemy import cast, String
from app.core.cloudinary_config import upload_image

def create_legend(session: Session, data: LegendCreate) -> Legend:
    legend = Legend(
        id=uuid4(),
        name=data.name,
        description=data.description,
        legend_date=data.legend_date,
        image_url=data.image_url,
        category_id=data.category_id,
        location_id=data.location_id,
    )
    return legend_repository.create_legend(session, legend)

def get_legends(
    session: Session,
    name: Optional[str],
    category_id: Optional[UUID],
    province_id: Optional[UUID],
    canton_id: Optional[UUID],
    district_id: Optional[UUID],
):
    query = select(Legend)

    if name:
        query = select(Legend).where(cast(Legend.name, String).ilike(f"%{name}%"))
    if category_id:
        query = query.where(Legend.category_id == category_id)
    if province_id:
        query = query.join(Location).where(Location.province_id == province_id)
    if canton_id:
        query = query.join(Location).where(Location.canton_id == canton_id)
    if district_id:
        query = query.join(Location).where(Location.district_id == district_id)

    return session.exec(query).all()

def fetch_legend_by_id(session: Session, legend_id: UUID):
    return legend_repository.get_legend_by_id(session, legend_id)


def update_legend(
    session: Session,
    legend_id:  UUID,
    name: Optional[str],
    description: Optional[str],
    legend_date: Optional[date],
    category_id: Optional[UUID],
    location_id: Optional[UUID],
    image: Optional[UploadFile],
):
    legend = legend_repository.get_legend_by_id(session, legend_id)
    if not legend:
        raise HTTPException(status_code=404, detail="Legend not found")

    if name is not None:
        legend.name = name
    if description is not None:
        legend.description = description
    if legend_date is not None:
        legend.legend_date = legend_date
    if category_id is not None:
        legend.category_id = category_id
    if location_id is not None:
        legend.location_id = location_id
    if image:
        image_url = upload_image(image)
        legend.image_url = image_url

    return legend_repository.update_legend(session, legend)