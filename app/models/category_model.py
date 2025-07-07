from typing import TYPE_CHECKING
from sqlmodel import Relationship, SQLModel, Field
from uuid import uuid4
class Category(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    name: str