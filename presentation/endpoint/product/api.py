from decimal import Decimal

from fastapi import APIRouter

from .out_schemas import GetProductsResponse, Product

router = APIRouter()


@router.get("/products")
def get_products() -> GetProductsResponse:
    products: list[Product] = list()
    products.append(Product(id=1, name="상품01", price=Decimal("100000")))
    products.append(Product(id=2, name="상품02", price=Decimal("200000")))
    return GetProductsResponse(items=products)
