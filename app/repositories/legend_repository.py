from typing import Optional
from sqlalchemy import String, cast
from sqlmodel import Session, select
from app.models.legend_model import Legend
from app.models.location_model import Location
from sqlalchemy.orm import selectinload

def create_legend(session: Session, legend: Legend) -> Legend:
    session.add(legend)
    session.commit()
    session.refresh(legend)
    return legend

def get_legend_by_id(session: Session, legend_id: str) -> Legend | None:
    return session.exec(
        select(Legend).where(Legend.id == legend_id)
    ).first()
    
def update_legend(session: Session, legend: Legend) -> Legend:
    session.add(legend)
    session.commit()
    session.refresh(legend)
    return legend

def delete_legend(session: Session, legend: Legend) -> None:
    session.delete(legend)
    session.commit()
    
def get_all_legends(session: Session, 
    name: Optional[str],
    category_id: Optional[str],
    province_id: Optional[str],
    canton_id: Optional[str],
    district_id: Optional[str]
):
    
    query = select(Legend).options(
            selectinload(Legend.category), # type: ignore
            selectinload(Legend.location) # type: ignore
        )

    if name:
        query = query.where(cast(Legend.name, String).ilike(f"%{name}%"))
    if category_id:
        query = query.where(Legend.category_id == category_id)
    if province_id or canton_id or district_id:
        query = query.join(Location)

        if province_id:
            query = query.where(Location.province_id == province_id)
        if canton_id:
            query = query.where(Location.canton_id == canton_id)
        if district_id:
            query = query.where(Location.district_id == district_id)

    return session.exec(query).all()