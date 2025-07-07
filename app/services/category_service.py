from sqlmodel import Session
from app.repositories import category_repository

def get_categories(session: Session):
    return category_repository.get_all_categories(session)