from pydantic import BaseModel
from uuid import UUID


class ProvinceResponse(BaseModel):
    id: UUID
    name: str

    class Config:
        from_attributes = True

class CantonResponse(BaseModel):
    id: UUID
    name: str
    province_id: UUID

    class Config:
        from_attributes = True

class DistrictResponse(BaseModel):
    id: UUID
    name: str
    canton_id: UUID

    class Config:
        from_attributes = True

class LocationResponse(BaseModel):
    id: UUID
    province_id: UUID
    canton_id: UUID
    district_id: UUID

    class Config:
        from_attributes = True
