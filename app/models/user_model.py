from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID

class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    name: str
    email: str = Field(index=True, unique=True)
    hashed_password: str
