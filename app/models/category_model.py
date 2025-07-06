from typing import TYPE_CHECKING
from sqlmodel import Relationship, SQLModel, Field
from uuid import UUID, uuid4

if TYPE_CHECKING:
    from app.models.legend_model import Legend
class Category(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    legends: list["Legend"] = Relationship(back_populates="category")