from fastapi import APIRouter
from app.services.hello_service import get_hello_message

router = APIRouter(
    prefix="/hello",
    tags=["Hello"]
)

@router.get("")
def say_hello():
    return {"message": get_hello_message()}
