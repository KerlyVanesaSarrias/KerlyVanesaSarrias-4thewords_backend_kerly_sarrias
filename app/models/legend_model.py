from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import date

class Legend(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    description: str
    image_url: Optional[str]
    legend_date: date
    category_id: UUID = Field(foreign_key="category.id")
    location_id: UUID = Field(foreign_key="location.id")
