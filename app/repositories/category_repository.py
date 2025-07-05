from sqlmodel import Session, select
from app.models.category_model import Category

def get_all_categories(session: Session):
    return session.exec(select(Category)).all()