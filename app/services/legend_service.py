from sqlmodel import Session
from app.models.legend_model import Legend
from app.schemas.legend_schema import LegendCreate
from app.repositories import legend_repository
from uuid import uuid4

def create_legend(session: Session, data: LegendCreate) -> Legend:
    legend = Legend(
        id=uuid4(),
        name=data.name,
        description=data.description,
        legend_date=data.legend_date,
        image_url=data.image_url,
        category_id=data.category_id,
        location_id=data.location_id,
    )
    return legend_repository.create_legend(session, legend)

