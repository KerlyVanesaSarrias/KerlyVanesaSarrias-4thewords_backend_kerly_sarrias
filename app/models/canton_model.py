from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

class Canton(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    province_id: UUID = Field(foreign_key="province.id")
