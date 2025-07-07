from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.services import category_service
from app.schemas.category_schema import CategoryResponse

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("", response_model=list[CategoryResponse])
def list_categories(session: Session = Depends(get_session)):
    return category_service.get_categories(session)