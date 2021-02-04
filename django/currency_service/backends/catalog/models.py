from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Product:
    sku: str
    seller: str
    price: Decimal
    old_price: Decimal = None
    cash_price: Decimal = None
