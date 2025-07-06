from typing import TYPE_CHECKING
from sqlmodel import Relationship, SQLModel, Field
from uuid import UUID, uuid4

if TYPE_CHECKING:
    from app.models.legend_model import Legend

class Location(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    province_id: UUID = Field(foreign_key="province.id")
    canton_id: UUID = Field(foreign_key="canton.id")
    district_id: UUID = Field(foreign_key="district.id")
    legends: list["Legend"] = Relationship(back_populates="location")
