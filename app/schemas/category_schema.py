from pydantic import BaseModel


class CategoryResponse(BaseModel):
    id: str
    name: str

    class Config:
        from_attributes = True