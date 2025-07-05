from select import select
from typing import Optional
from sqlmodel import Session
from app.models.legend_model import Legend
from app.schemas.legend_schema import LegendCreate
from app.repositories import legend_repository
from uuid import UUID, uuid4
from typing import Optional, List
from sqlmodel import Session, select
from app.models.legend_model import Legend
from app.models.category_model import Category
from app.models.location_model import Location
from sqlalchemy import cast, String

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

