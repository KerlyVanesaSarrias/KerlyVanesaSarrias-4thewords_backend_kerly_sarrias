from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

class District(SQLModel, table=True):
    id:UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    canton_id: UUID = Field(foreign_key="canton.id")