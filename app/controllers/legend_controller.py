from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.legend_model import Legend
from app.services import legend_service
from app.schemas.legend_schema import LegendCreate, LegendResponse, LegendUpdate
from datetime import date
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
    category_id: str = Form(...),
    province_id: str = Form(...),
    canton_id: str = Form(...),
    district_id: str = Form(...),
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
        "province_id": province_id,
        "canton_id": canton_id,
        "district_id": district_id,
        "image_url": image_url,
    }

    legend = legend_service.create_legend(session, data=LegendCreate(**legend_data))
    return legend

@router.get("/", response_model=List[LegendResponse])
def get_legends(
    session: Session = Depends(get_session),
    name: Optional[str] = None,
    category_id: Optional[str] = None,
    province_id: Optional[str] = None,
    canton_id: Optional[str] = None,
    district_id: Optional[str] = None,
    legend_date: Optional[date] = None,
    current_user: User = Depends(get_current_user)
    
):
    return legend_service.get_legends(
        session, name, category_id, province_id, canton_id, district_id, legend_date
    )

@router.get("/{legend_id}", response_model=LegendResponse)
def get_legend_by_id(legend_id: str, session: Session = Depends(get_session)):
    legend = legend_service.fetch_legend_by_id(session, legend_id)
    if not legend:
        raise HTTPException(status_code=404, detail="Legend not found")
    return legend



@router.put("/{legend_id}", response_model=LegendResponse)
def update_legend(
    legend_id: str,
    name: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    legend_date: Optional[date] = Form(None),
    category_id: Optional[str] = Form(None),
    location_id: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None),
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return legend_service.update_legend(
        session=session,
        legend_id=legend_id,
        name=name,
        description=description,
        legend_date=legend_date,
        category_id=category_id,
        location_id=location_id,
        image=image
    )
    

@router.delete("/{legend_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_legend(
    legend_id: str,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    result = legend_service.delete_legend(session, legend_id)
    return JSONResponse(status_code=200, content=result)
    