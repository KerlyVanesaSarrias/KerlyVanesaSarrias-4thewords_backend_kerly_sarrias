from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings

engine = create_engine(settings.db_url, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    from app.models import (
        user_model,
        category_model,
        province_model,
        canton_model,
        district_model,
        legend_model
    )
    SQLModel.metadata.create_all(engine)

