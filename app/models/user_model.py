from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field
from uuid import uuid4

class User(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    name: str
    email: str = Field(index=True, unique=True)
    hashed_password: str
