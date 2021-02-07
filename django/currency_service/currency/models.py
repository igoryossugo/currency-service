from dataclasses import dataclass
from decimal import Decimal

from django.conf import settings

from currency_service.backends.pools.cotation import CotationBackendPool
from currency_service.currency.enums import CurrencyID
from currency_service.models import BaseModel


@dataclass
class Currency(BaseModel):
    id: CurrencyID
    value: Decimal

    def convert(self, id: CurrencyID):
        if id == self.id:
            return

        cotation_backend = CotationBackendPool.get_default()
        cotation = cotation_backend.get(
            target_currency=id,
            source_currency=self.id
        )
        self.id = id
        self.value = self.value / cotation.value

    @classmethod
    def convert_list(cls, id: CurrencyID, value: Decimal):
        currencies = []
        for currency_id in settings.DEFAULT_CONVERT_CURRENCY_IDS:
            currency = cls(id=id, value=value)
            currency.convert(id=currency_id)
            currencies.append(currency)

        return currencies
