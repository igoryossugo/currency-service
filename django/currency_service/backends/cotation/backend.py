from abc import abstractmethod
from typing import List

from currency_service.currency.models import Currency
from currency_service.currency.enums import CurrencyID


class CotationBackend:
    id = None
    name = None

    @abstractmethod
    def get(
        self,
        currency: Currency,
        currency_id: CurrencyID
    ) -> Currency:
        pass

    @abstractmethod
    def list(
        self,
        currency: Currency,
        currency_ids: List[CurrencyID] = None
    ) -> List[Currency]:
        pass
