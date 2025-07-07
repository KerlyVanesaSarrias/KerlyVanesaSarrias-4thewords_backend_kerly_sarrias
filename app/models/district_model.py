from sqlmodel import SQLModel, Field
from uuid import uuid4

class District(SQLModel, table=True):
    id:str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    name: str
    canton_id: str = Field(foreign_key="canton.id")