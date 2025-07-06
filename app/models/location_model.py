from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

class Location(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    province_id: UUID = Field(foreign_key="province.id")
    canton_id: UUID = Field(foreign_key="canton.id")
    district_id: UUID = Field(foreign_key="district.id")
