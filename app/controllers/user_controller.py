from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.database import get_session
from app.schemas.user_schema import UserCreate, UserResponse, UserLogin
from app.services import user_service
from app.core.security import create_access_token
router = APIRouter(prefix="/auth", tags=["Auth"])
from app.utils.auth_utils import get_current_user
from app.models.user_model import User

@router.post("/register", response_model=UserResponse)
def register(data: UserCreate, session: Session = Depends(get_session)):
    user = user_service.create_user(session, data)
    return user

@router.post("/login")
def login(data: UserLogin, session: Session = Depends(get_session)):
    user = user_service.authenticate_user(session, data.email, data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user