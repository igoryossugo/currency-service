from dataclasses import dataclass
from decimal import Decimal

from currency_service.currency.enums import CurrencyID


@dataclass
class Currency:
    id: CurrencyID
    value: Decimal
