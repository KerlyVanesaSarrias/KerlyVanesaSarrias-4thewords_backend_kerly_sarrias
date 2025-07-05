import uuid
import cloudinary
import cloudinary.uploader
from fastapi import UploadFile
from app.core.config import settings

cloudinary.config(
    cloud_name=settings.cloudinary_cloud_name,
    api_key=settings.cloudinary_api_key,
    api_secret=settings.cloudinary_api_secret
)

def upload_image(file: UploadFile) -> str:
    """
    Sube una imagen a Cloudinary y retorna la URL.
    """
    file_bytes = file.file.read()
    file.file.seek(0)  

    result = cloudinary.uploader.upload(
        file_bytes,
        public_id=str(uuid.uuid4()),
        folder="legends_images"
    )
    return result["secure_url"]