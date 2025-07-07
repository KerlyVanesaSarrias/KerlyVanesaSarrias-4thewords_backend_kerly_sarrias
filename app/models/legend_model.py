from sqlmodel import Relationship, SQLModel, Field
from typing import Optional
from uuid import uuid4
from datetime import date

from app.models.category_model import Category
from app.models.location_model import Location

class Legend(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    name: str
    description: str
    image_url: Optional[str]
    legend_date: date
    category_id: str = Field(foreign_key="category.id")
    location_id: str = Field(foreign_key="location.id")
    category: Optional[Category] = Relationship(back_populates="legends")
    location: Optional[Location] = Relationship(back_populates="legends")