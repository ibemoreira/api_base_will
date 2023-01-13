from fastapi import APIRouter
from api.V1.endpoints import ft_rgb
 
api_router = APIRouter()

api_router.include_router(ft_rgb.router, prefix="/cor-predominante", tags=["RGB"])

