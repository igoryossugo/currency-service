from abc import abstractmethod

from django.conf import settings
from django.core.cache import caches

from currency_service.backends.cotation.constants import (
    DEFAULT_LOCAL_CURRENCY_ID
)
from currency_service.backends.cotation.models import Cotation
from currency_service.currency.enums import CurrencyID

cache = caches['cotation']


class CotationBackend:
    id = None
    name = None

    def get(
        self,
        target_currency: CurrencyID,
        source_currency: CurrencyID = DEFAULT_LOCAL_CURRENCY_ID,
    ) -> Cotation:
        cache_key = f'{target_currency}_{source_currency}'
        cotation = cache.get(cache_key)
        if cotation:
            return cotation

        cotation = self._get(
            target_currency=target_currency,
            source_currency=source_currency
        )
        cache.set(cache_key, cotation, settings.CACHE_LIFETIME['cotation'])
        return cotation

    @abstractmethod
    def _get(
        self,
        target_currency: CurrencyID,
        source_currency: CurrencyID = DEFAULT_LOCAL_CURRENCY_ID,
    ) -> Cotation:
        pass
