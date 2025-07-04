from sqlmodel import Session
from app.models.user_model import User
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def create_user(session: Session, user: User):
    try:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=400, detail="El email ya está registrado.")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear usuario: {str(e)}")