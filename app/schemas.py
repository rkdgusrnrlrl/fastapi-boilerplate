from decimal import Decimal

from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: Decimal


class GetProductsResponse(BaseModel):
    items: list[Product]