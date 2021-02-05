from decimal import Decimal

from ramos.mixins import SingletonCreateMixin

from currency_service.backends.cotation.backend import CotationBackend
from currency_service.backends.cotation.models import Cotation
from currency_service.currency.constants import DEFAULT_LOCAL_CURRENCY_ID


class FakeCotationBackend(SingletonCreateMixin, CotationBackend):
    id = 'fake'
    name = 'Fake'

    def _get(self, target_currency, source_currency=DEFAULT_LOCAL_CURRENCY_ID):
        return Cotation(
            value=Decimal('5.72'),
            source_currency=source_currency,
            target_currency=target_currency,
        )
