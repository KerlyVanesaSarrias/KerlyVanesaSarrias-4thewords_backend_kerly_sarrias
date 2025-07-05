from uuid import UUID
from sqlmodel import Session, select
from app.models.legend_model import Legend

def create_legend(session: Session, legend: Legend) -> Legend:
    session.add(legend)
    session.commit()
    session.refresh(legend)
    return legend

def get_legend_by_id(session: Session, legend_id: str) -> Legend | None:
    return session.exec(
        select(Legend).where(Legend.id == UUID(legend_id))
    ).first()