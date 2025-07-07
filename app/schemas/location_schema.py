from pydantic import BaseModel

class ProvinceCreate(BaseModel):
    name: str

class ProvinceResponse(BaseModel):
    id: str
    name: str

    class Config:
        from_attributes = True

class CantonCreate(BaseModel):
    name: str
    province_id: str
class CantonResponse(BaseModel):
    id: str
    name: str
    province_id: str

    class Config:
        from_attributes = True

class DistrictCreate(BaseModel):
    name: str
    canton_id: str

class DistrictResponse(BaseModel):
    id: str
    name: str
    canton_id: str

    class Config:
        from_attributes = True

class LocationResponse(BaseModel):
    id: str
    province_id: str
    canton_id: str
    district_id: str

    class Config:
        from_attributes = True
