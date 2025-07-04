from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6, max_length=50)


class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr

class Config:
    from_attributes = True
