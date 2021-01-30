from dataclasses import dataclass
from decimal import Decimal

from currency_service.currency.enums import CurrencyID


@dataclass
class Cotation:
    value: Decimal
    source_currency: CurrencyID
    target_currency: CurrencyID
