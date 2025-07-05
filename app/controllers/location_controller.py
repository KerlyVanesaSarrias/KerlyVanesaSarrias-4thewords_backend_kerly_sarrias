from uuid import UUID
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from app.core.database import get_session
from app.models.user_model import User
from app.repositories.location_repository import (
    get_all_provinces, get_cantons_by_province, get_districts_by_canton
)
from app.schemas.location_schema import ProvinceResponse, CantonResponse, DistrictResponse
from app.utils.auth_utils import get_current_user

router = APIRouter(prefix="/locations", tags=["Locations"])

@router.get("/provinces", response_model=list[ProvinceResponse])
def list_provinces(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
    ):
    return get_all_provinces(session)

@router.get("/cantons", response_model=list[CantonResponse])
def list_cantons(
    province_id: UUID = Query(...), 
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return get_cantons_by_province(session, province_id)

@router.get("/districts", response_model=list[DistrictResponse])
def list_districts(
    canton_id: UUID = Query(...), 
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return get_districts_by_canton(session, canton_id)
