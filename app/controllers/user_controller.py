from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.database import get_session
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse
from app.services import user_service
from typing import List

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register(data: UserCreate, session: Session = Depends(get_session)):
    user = user_service.create_user(session, data)
    return user

