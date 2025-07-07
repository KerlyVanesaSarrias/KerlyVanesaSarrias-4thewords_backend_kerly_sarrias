from datetime import date
from select import select
from typing import Optional
from fastapi import HTTPException, UploadFile
from sqlmodel import Session
from app.models.legend_model import Legend
from app.schemas.legend_schema import LegendCreate, LegendResponse, LegendUpdate
from app.repositories import legend_repository
from typing import Optional, List
from sqlmodel import Session, select
from app.models.legend_model import Legend
from app.core.cloudinary_config import upload_image

def create_legend(session: Session, data: LegendCreate) -> Legend:
    legend = Legend(
        name=data.name,
        description=data.description,
        legend_date=data.legend_date,
        image_url=data.image_url,
        category_id=data.category_id,
        province_id=data.province_id,
        canton_id=data.canton_id,
        district_id=data.district_id
    )
    return legend_repository.create_legend(session, legend)

def get_legends(
    session: Session,
    name: Optional[str],
    category_id: Optional[str],
    province_id: Optional[str],
    canton_id: Optional[str],
    district_id: Optional[str],
):
    legends = legend_repository.get_all_legends(
        session,
        name=name,
        category_id=category_id,
        province_id=province_id,
        canton_id=canton_id,
        district_id=district_id
    )
    print(f"Legends fetched: {legends}")
    return legends

def fetch_legend_by_id(session: Session, legend_id: str):
    return legend_repository.get_legend_by_id(session, legend_id)


def update_legend(
    session: Session,
    legend_id:  str,
    name: Optional[str],
    description: Optional[str],
    legend_date: Optional[date],
    category_id: Optional[str],
    location_id: Optional[str],
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

def delete_legend(session: Session, legend_id: str):
    legend = legend_repository.get_legend_by_id(session, legend_id)
    if not legend:
        raise HTTPException(status_code=404, detail="Legend not found")

    legend_repository.delete_legend(session, legend)
    return {"message": "Legend deleted successfully"}