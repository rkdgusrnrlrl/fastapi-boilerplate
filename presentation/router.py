from fastapi import APIRouter
from .endpoint.product.api import router as product_router

router = APIRouter(prefix="/v1")
router.include_router(product_router)
