from abc import abstractmethod

from currency_service.backends.cotation.constants import (
    DEFAULT_LOCAL_CURRENCY_ID
)
from currency_service.backends.cotation.models import Cotation
from currency_service.currency.enums import CurrencyID


class CotationBackend:
    id = None
    name = None

    @abstractmethod
    def get(
        self,
        target_currency: CurrencyID,
        source_currency: CurrencyID = DEFAULT_LOCAL_CURRENCY_ID,
    ) -> Cotation:
        pass
