from dataclasses import dataclass
from decimal import Decimal

from currency_service.backends.pools.cotation import CotationBackendPool
from currency_service.currency.enums import CurrencyID


@dataclass
class Currency:
    id: CurrencyID
    value: Decimal

    def converter(self, id: CurrencyID):
        if id == self.id:
            return

        cotation_backend = CotationBackendPool.get_default()
        cotation = cotation_backend.get(
            target_currency=id,
            source_currency=self.id
        )
        self.id = id
        self.value = self.value * cotation.value
