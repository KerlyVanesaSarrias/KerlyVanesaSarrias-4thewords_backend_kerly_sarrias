from sqlmodel import SQLModel, Field
from uuid import uuid4

class Province(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    name: str
