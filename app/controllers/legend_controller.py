from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlmodel import Session
from app.core.database import get_session
from app.services import legend_service
from app.schemas.legend_schema import LegendCreate, LegendResponse
from datetime import date
from uuid import UUID
import cloudinary.uploader
from typing import List, Optional
from app.core.cloudinary_config import cloudinary
from app.models.user_model import User
from app.utils.auth_utils import get_current_user

router = APIRouter(prefix="/legends", tags=["Legends"])

@router.post("/", response_model=LegendResponse)
async def create_legend_endpoint(
    name: str = Form(...),
    description: str = Form(...),
    legend_date: date = Form(...),
    category_id: UUID = Form(...),
    location_id: UUID = Form(...),
    image: UploadFile = File(...),
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    try:
        result = cloudinary.uploader.upload(image.file, folder="leyendas")
        image_url = result["secure_url"]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al subir imagen: " + str(e))

    legend_data = {
        "name": name,
        "description": description,
        "legend_date": legend_date,
        "category_id": category_id,
        "location_id": location_id,
        "image_url": image_url,
    }

    legend = legend_service.create_legend(session, data=LegendCreate(**legend_data))
    return legend

@router.get("/", response_model=List[LegendResponse])
def get_legends(
    session: Session = Depends(get_session),
    name: Optional[str] = None,
    category_id: Optional[UUID] = None,
    province_id: Optional[UUID] = None,
    canton_id: Optional[UUID] = None,
    district_id: Optional[UUID] = None,
    current_user: User = Depends(get_current_user)
):
    return legend_service.get_legends(
        session, name, category_id, province_id, canton_id, district_id
    )
