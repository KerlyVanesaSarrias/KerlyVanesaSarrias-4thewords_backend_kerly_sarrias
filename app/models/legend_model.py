from sqlmodel import Relationship, SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import date

from app.models.category_model import Category
from app.models.location_model import Location

class Legend(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    description: str
    image_url: Optional[str]
    legend_date: date
    category_id: UUID = Field(foreign_key="category.id")
    location_id: UUID = Field(foreign_key="location.id")
    category: Optional[Category] = Relationship(back_populates="legends")
    location: Optional[Location] = Relationship(back_populates="legends")