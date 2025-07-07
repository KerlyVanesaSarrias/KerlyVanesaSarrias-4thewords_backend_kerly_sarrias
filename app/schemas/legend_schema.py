from pydantic import BaseModel
from typing import Optional
from datetime import date

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: str

    class Config:
        from_attributes = True

class ProvinceBase(BaseModel):
    name: str

class ProvinceCreate(ProvinceBase):
    pass

class ProvinceResponse(ProvinceBase):
    id: str

    class Config:
        from_attributes = True


class CantonBase(BaseModel):
    name: str
    province_id: str

class CantonCreate(CantonBase):
    pass

class CantonResponse(CantonBase):
    id: str

    class Config:
        from_attributes = True


class DistrictBase(BaseModel):
    name: str
    canton_id: str

class DistrictCreate(DistrictBase):
    pass

class DistrictResponse(DistrictBase):
    id: str

    class Config:
        from_attributes = True

class LocationBase(BaseModel):
    province_id: str
    canton_id: str
    district_id: str

class LocationCreate(LocationBase):
    pass

class LocationResponse(LocationBase):
    id: str

    class Config:
        from_attributes = True


class LegendBase(BaseModel):
    name: str
    description: str
    legend_date: date
    category_id: str
    location_id: str
    image_url: Optional[str] = None

class LegendCreate(LegendBase):
    pass

class LegendResponse(LegendBase):
    id: str

    class Config:
        from_attributes = True


class LegendUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    legend_date: Optional[date]
    category_id: Optional[str]
    location_id: Optional[str]

    class Config:
        from_attributes = True