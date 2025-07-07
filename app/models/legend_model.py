from sqlalchemy import Column, ForeignKey, String
from sqlmodel import Relationship, SQLModel, Field
from typing import TYPE_CHECKING, Optional
from uuid import uuid4
from datetime import date

if TYPE_CHECKING:
    from app.models.category_model import Category
    from app.models.province_model import Province
    from app.models.canton_model import Canton
    from app.models.district_model import District
    
class Legend(SQLModel, table=True):
    id: str = Field(
        default_factory=lambda: str(uuid4()),
        sa_column=Column(String(36), primary_key=True)
    )
    name: str
    description: str
    image_url: Optional[str]
    legend_date: date
    category_id: str = Field(sa_column=Column(String(36), ForeignKey("category.id"), nullable=False, index=True))
    province_id: str = Field(sa_column=Column(String(36), ForeignKey("province.id"), nullable=False, index=True))
    canton_id: str = Field(sa_column=Column(String(36), ForeignKey("canton.id"), nullable=False, index=True))
    district_id: str = Field(sa_column=Column(String(36), ForeignKey("district.id"), nullable=False, index=True))
    category: Optional["Category"] = Relationship()
    province: Optional["Province"] = Relationship()
    canton: Optional["Canton"] = Relationship()
    district: Optional["District"] = Relationship()