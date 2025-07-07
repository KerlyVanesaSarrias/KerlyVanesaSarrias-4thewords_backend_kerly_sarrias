from sqlmodel import SQLModel, Field
from uuid import uuid4

class Canton(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    name: str
    province_id: str = Field(foreign_key="province.id")
