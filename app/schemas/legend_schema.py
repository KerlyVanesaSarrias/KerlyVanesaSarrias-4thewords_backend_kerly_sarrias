from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import date

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: UUID

    class Config:
        from_attributes = True

class ProvinceBase(BaseModel):
    name: str

class ProvinceCreate(ProvinceBase):
    pass

class ProvinceResponse(ProvinceBase):
    id: UUID

    class Config:
        from_attributes = True


class CantonBase(BaseModel):
    name: str
    province_id: UUID

class CantonCreate(CantonBase):
    pass

class CantonResponse(CantonBase):
    id: UUID

    class Config:
        from_attributes = True


class DistrictBase(BaseModel):
    name: str
    canton_id: UUID

class DistrictCreate(DistrictBase):
    pass

class DistrictResponse(DistrictBase):
    id: UUID

    class Config:
        from_attributes = True

class LocationBase(BaseModel):
    province_id: UUID
    canton_id: UUID
    district_id: UUID

class LocationCreate(LocationBase):
    pass

class LocationResponse(LocationBase):
    id: UUID

    class Config:
        from_attributes = True


class LegendBase(BaseModel):
    name: str
    description: str
    legend_date: date
    category_id: UUID
    location_id: UUID
    image_url: Optional[str] = None

class LegendCreate(LegendBase):
    pass

class LegendResponse(LegendBase):
    id: UUID

    class Config:
        from_attributes = True
