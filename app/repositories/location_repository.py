from sqlmodel import Session, select
from app.models import canton_model, district_model, province_model
from uuid import UUID

def get_all_provinces(session: Session):
    return session.exec(select(province_model.Province)).all()

def get_cantons_by_province(session: Session, province_id: UUID):
    return session.exec(select(canton_model.Canton).where(canton_model.Canton.id == province_id)).all()

def get_districts_by_canton(session: Session, canton_id: UUID):
    return session.exec(select(district_model.District).where(district_model.District.id == canton_id)).all()
