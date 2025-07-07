from typing import TYPE_CHECKING
from sqlmodel import Relationship, SQLModel, Field
from uuid import uuid4

if TYPE_CHECKING:
    from app.models.legend_model import Legend
class Category(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    name: str
    legends: list["Legend"] = Relationship(back_populates="category")