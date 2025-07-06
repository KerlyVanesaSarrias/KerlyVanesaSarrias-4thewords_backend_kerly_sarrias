from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.repositories.category_repository import get_all_categories
from app.schemas.category_schema import CategoryResponse

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("", response_model=list[CategoryResponse])
def list_categories(session: Session = Depends(get_session)):
    return get_all_categories(session)