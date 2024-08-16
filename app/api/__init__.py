from fastapi import APIRouter
from .routers import products

api_router = APIRouter()
api_router.include_router(products.router, tags=["products"])