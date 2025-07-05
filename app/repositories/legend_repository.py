from sqlmodel import Session
from app.models.legend_model import Legend

def create_legend(session: Session, legend: Legend) -> Legend:
    session.add(legend)
    session.commit()
    session.refresh(legend)
    return legend
