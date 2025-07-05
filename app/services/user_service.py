from sqlmodel import Session, select
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password, verify_password
from app.repositories import user_repository

def create_user(session: Session, user_data: UserCreate):
    hashed = hash_password(user_data.password)
    user = User(email = user_data.email, name=user_data.name, hashed_password=hashed)
    userCreated = user_repository.create_user(session, user)
    return userCreated

def authenticate_user(session: Session, email: str, password: str):
    user = session.exec(select(User).where(User.email == email)).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


