from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from app.core.database import get_session
from app.models.user_model import User
from app.repositories import location_repository
from app.schemas.location_schema import CantonCreate, DistrictCreate, LocationResponse, ProvinceCreate, ProvinceResponse, CantonResponse, DistrictResponse
from app.utils.auth_utils import get_current_user

router = APIRouter(prefix="/locations", tags=["Locations"])

@router.get("/provinces", response_model=list[ProvinceResponse])
def list_provinces(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
    ):
    return location_repository.get_all_provinces(session)

@router.get("/province/{province_id}/cantons", response_model=list[CantonResponse])
def list_cantons_by_province(
    province_id: str, 
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return location_repository.get_cantons_by_province(session, province_id)

@router.get("/canton/{canton_id}/districts", response_model=list[DistrictResponse])
def list_districts_by_canton(
    canton_id: str, 
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return location_repository.get_districts_by_canton(session, canton_id)

@router.get("/districts", response_model=list[DistrictResponse])
def list_districts(
    canton_id: str = Query(...), 
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return location_repository.get_districts_by_canton(session, canton_id)

@router.post("/province", response_model=ProvinceResponse)
def create_province(
    province: ProvinceCreate, 
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    provinceCreated = location_repository.create_province(session, province.name)
    return provinceCreated

@router.post("/canton", response_model=CantonResponse)
def create_canton(
    canton: CantonCreate, 
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    cantonCreated = location_repository.create_canton(session, canton.name, canton.province_id)
    return cantonCreated

@router.post("/district", response_model=DistrictResponse)
def create_district(
    district: DistrictCreate, 
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    districtCreated = location_repository.create_district(session, district.name, district.canton_id)
    return districtCreated
