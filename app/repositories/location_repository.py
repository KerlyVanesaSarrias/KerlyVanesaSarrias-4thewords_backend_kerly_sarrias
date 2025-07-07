from fastapi import HTTPException
from sqlmodel import Session, select
from app.models import canton_model, district_model, province_model, location_model

def get_all_provinces(session: Session):
    return session.exec(select(province_model.Province)).all()

def get_cantons_by_province(session: Session, province_id: str):
    print(f"Fetching cantons for province ID: {province_id}")
    return session.exec(select(canton_model.Canton).where(canton_model.Canton.province_id == province_id)).all()

def get_districts_by_canton(session: Session, canton_id: str):
    return session.exec(select(district_model.District).where(district_model.District.canton_id == canton_id)).all()

def get_location_by_id(session: Session, location_id: str):
    location = session.exec(
        select(location_model.Location).where(location_model.Location.id == location_id)
    ).first()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

def create_province(session: Session, name: str):
    province = province_model.Province(name=name)
    session.add(province)
    session.commit()
    session.refresh(province)
    return province

def create_canton(session: Session, name: str, province_id: str):
    canton = canton_model.Canton(name=name, province_id=province_id)
    session.add(canton)
    session.commit()
    session.refresh(canton)
    return canton

def create_district(session: Session, name: str, canton_id: str):
    district = district_model.District(name=name, canton_id=canton_id)
    session.add(district)
    session.commit()
    session.refresh(district)
    return district