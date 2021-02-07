from dataclasses import dataclass
from decimal import Decimal

from currency_service.currency.constants import DEFAULT_LOCAL_CURRENCY_ID
from currency_service.currency.models import Currency


@dataclass
class Product:
    sku: str
    seller: str
    price: Decimal

    def list_currencies(self):
        return Currency.converter_list(
            id=DEFAULT_LOCAL_CURRENCY_ID,
            value=self.price
        )
